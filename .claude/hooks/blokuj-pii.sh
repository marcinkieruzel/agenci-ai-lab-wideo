#!/usr/bin/env bash
# Hook PreToolUse: blokuje bezpośredni dostęp agenta do pliku z danymi osobowymi.
# Claude Code przekazuje opis wywołania narzędzia jako JSON na stdin.
# Kod wyjścia 2 = zablokuj wywołanie; komunikat ze stderr trafia do Claude'a.
input=$(cat)
if echo "$input" | grep -q 'logi-z-pii' && ! echo "$input" | grep -q 'maskuj.py'; then
  echo "Zablokowano: logi-z-pii.log zawiera dane osobowe. Użyj: python3 maskuj.py logi-z-pii.log" >&2
  exit 2
fi
exit 0
