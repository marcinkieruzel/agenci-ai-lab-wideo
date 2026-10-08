# Agenci AI na platformie wideo — lab (dane fikcyjne)

Materiały do ćwiczeń ze szkolenia „Agenci AI i infrastruktura Claude”: fikcyjny incydent platformy
streamingowej, logi do analizy i gotowa konfiguracja Claude Code (pamięć, skill, subagent, hook).

**Wszystkie dane są wygenerowane na potrzeby szkolenia.** Numery telefonów mają format `+48 0xx …`
(w Polsce żaden numer nie zaczyna się od zera), adresy IP pochodzą z puli zarezerwowanej dla dokumentacji
(RFC 5737), a identyfikatory i tokeny są losowe.

## Zawartość

| Plik | Do czego |
| --- | --- |
| `incydent-INC-2417.md` | zgłoszenie do ćwiczenia: buforowanie na kanale sport-1 w trakcie meczu |
| `cdn-edge.log`, `player-errors.log`, `encoder-alerts.log` | logi do analizy |
| `zmiany-konfiguracji.md` | dziennik zmian z wieczoru incydentu |
| `logi-z-pii.log` | zgłoszenia z „danymi osobowymi” — do ćwiczenia z maskowania |
| `maskuj.py` | maskowanie danych osobowych: `python3 maskuj.py logi-z-pii.log` |
| `CLAUDE.md` | pamięć projektu: architektura, priorytety P1–P4, zasady pracy, format raportu |
| `.claude/skills/triage-incydentu/SKILL.md` | skill z procedurą triage |
| `.claude/agents/analityk-logow.md` | subagent do liczenia w logach |
| `.claude/settings.json`, `.claude/hooks/blokuj-pii.sh` | hook blokujący bezpośredni dostęp do pliku z danymi osobowymi |

## Wymagania

- [Claude Code](https://code.claude.com/docs) z kontem Claude (Pro, Max, Team lub Enterprise)
- Python 3 (dla `maskuj.py`), bash (dla hooka)
- opcjonalnie [Ollama](https://ollama.com) — do ćwiczeń z modelem lokalnym

## Start

```bash
git clone https://github.com/marcinkieruzel/agenci-ai-lab-wideo.git
cd agenci-ai-lab-wideo
claude            # Shift+Tab → tryb Plan
> /context
> /triage-incydentu INC-2417
```

Uwaga: katalog zawiera hook (`.claude/settings.json`), który Claude Code uruchamia przy każdym użyciu
narzędzi Read, Grep i Bash. Przeczytaj `.claude/hooks/blokuj-pii.sh`, zanim zaufasz katalogowi — to dobra
praktyka przy każdym cudzym repozytorium z konfiguracją Claude Code.

## Model lokalny zamiast Claude (tylko do demonstracji)

Integracja po stronie Ollamy, nieoficjalna dla Claude Code. Model musi obsługiwać narzędzia i mieć okno
kontekstu co najmniej 64 tys. tokenów.

```bash
ollama launch claude --model qwen3-coder
# albo ręcznie:
ANTHROPIC_BASE_URL=http://localhost:11434 ANTHROPIC_AUTH_TOKEN=ollama ANTHROPIC_API_KEY="" \
  claude --model <model z oknem ≥ 64k>
```
