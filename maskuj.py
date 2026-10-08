#!/usr/bin/env python3
"""Maskuje dane osobowe w logach, zanim trafią do modelu w chmurze.

Użycie:  python3 maskuj.py logi-z-pii.log > logi-zamaskowane.log

Zasada: maskuje kod (deterministycznie), nie model. Ten sam abonent dostaje zawsze ten sam
pseudonim, więc da się liczyć powtórzenia, ale nie da się wrócić do numeru bez klucza.
Klucz (SALT) trzymaj poza repozytorium, np. w zmiennej środowiskowej.
"""
import hashlib
import hmac
import os
import re
import sys

SALT = os.environ.get("MASK_SALT", "zmien-mnie-na-szkoleniu").encode()


def pseudonim(prefix: str, value: str) -> str:
    digest = hmac.new(SALT, value.encode(), hashlib.sha256).hexdigest()[:8]
    return f"{prefix}-{digest}"


RULES = [
    # numer telefonu (MSISDN) -> pseudonim
    (re.compile(r"\+48[ \d]{9,12}\d"), lambda m: pseudonim("TEL", m.group().replace(" ", ""))),
    # identyfikator abonenta -> pseudonim
    (re.compile(r"SUB-\d+"), lambda m: pseudonim("ABO", m.group())),
    # identyfikator urządzenia -> pseudonim
    (re.compile(r"ATV-\d+"), lambda m: pseudonim("URZ", m.group())),
    # adres IP -> tylko sieć /24 (wystarczy do analizy regionu i operatora)
    (re.compile(r"\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.\d{1,3}\b"), lambda m: f"{m.group(1)}.{m.group(2)}.{m.group(3)}.0/24"),
    # tokeny DRM i sesji -> usunięte całkowicie
    (re.compile(r"(drm_token|token|session_token)=[0-9a-fA-F]{16,}"), lambda m: f"{m.group(1)}=[USUNIETO]"),
]


def maskuj(line: str) -> str:
    for pattern, repl in RULES:
        line = pattern.sub(repl, line)
    return line


if __name__ == "__main__":
    src = open(sys.argv[1], encoding="utf-8") if len(sys.argv) > 1 else sys.stdin
    for line in src:
        sys.stdout.write(maskuj(line))
