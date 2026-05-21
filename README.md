# Chatbot Projekt

## Beschreibung
Dieses Projekt ist ein interaktiver Konsolen-Chatbot.  
Der Benutzer kann Fragen aus verschiedenen Kategorien auswählen oder frei eingeben.  
Das System versucht passende Fragen automatisch zu erkennen und gibt passende Antworten aus.

---

## Funktionen

- Kategorienauswahl:
  - Projekt über AVL-Bäume
  - Leben
- Freie Eingabe von Fragen
- Ähnliche Fragen erkennen (Fuzzy Matching)
- Autovervollständigung bei Präfix-Eingaben
- Zufällige Frage („777“-Modus)
- Neustart des Chats ohne Programmneustart (`neu`)
- Beenden des Programms (`halt`, `stop`, `end`, `leave`)

---

## Projektstruktur

- `main.py` – Hauptprogramm (Chat-Loop)
- `introduction.py` – Begrüßungstext
- `Questions.py` – Kategorienlogik + Frage/Antwort-Verarbeitung
- `recommendationSystem.py` – Matching-System für ähnliche Fragen
- `PresentationInfo/`
  - `QuestionsList.txt` – Fragen zur Präsentation
  - `AnswersList.txt` – Antworten
- `LifeInfo/`
  - `QuestionsList.txt`
  - `AnswersList.txt`

---

## Benutzung

### Start
```bash
python main.py
