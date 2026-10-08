# INC-2417 — buforowanie na kanale sport-1 (dane fikcyjne, do ćwiczeń)

**Zgłoszono:** sob. 03.10.2026, 21:07, dyżur NOC
**Źródło:** wzrost zgłoszeń na infolinii + alert QoE „rebuffering ratio > 4%” dla Android TV

> Od ok. 21:05 klienci oglądający mecz na sport-1 zgłaszają zacinanie się obrazu, głównie na
> Android TV. Część mówi, że „wraca po kilku sekundach i znowu staje”. Inne kanały bez zgłoszeń.
> Nie wiemy, czy to CDN, enkoder czy aplikacja. Proszę o wstępną analizę i priorytet.

## Dostępne materiały

| Plik | Co zawiera |
|---|---|
| `cdn-edge.log` | logi dostępowe 12 serwerów brzegowych w Warszawie (20:50–21:40) |
| `player-errors.log` | błędy zgłaszane przez aplikacje (Android TV, Android, iOS, web, Tizen) |
| `encoder-alerts.log` | alerty i heartbeaty enkoderów |
| `zmiany-konfiguracji.md` | dziennik zmian z tego wieczoru |
| `logi-z-pii.log` | zgłoszenia z infolinii **z danymi osobowymi** — nie wysyłać do modelu przed maskowaniem |

## Zadanie dla zespołu

1. Sprawdź, czy dane są bezpieczne do wysłania (PII, tokeny). Zamaskuj, jeśli trzeba (`maskuj.py`).
2. Sklasyfikuj incydent (warstwa: enkoder / packager / origin / CDN / player / DRM) i nadaj priorytet P1–P4.
3. Postaw 2–3 hipotezy przyczyny i wskaż, które linie logów je potwierdzają lub obalają.
4. Zdecyduj, co sprawdza człowiek, zanim cokolwiek zmienimy na produkcji.
5. Przygotuj szkic komunikatu dla działu obsługi klienta i szkic postmortemu.
