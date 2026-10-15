# Changelog

Alle nennenswerten Änderungen an ARIA-Kompass. Die Einträge beschreiben, was das Projekt
danach kann bzw. was sich für den Nutzer ändert – kein Commit-Protokoll.

**Regel:** Jeder Commit bekommt seinen Eintrag, im selben Commit. Neues kommt oben unter
„Unveröffentlicht“ dazu; beim Release wird daraus ein Abschnitt mit Versionsnummer und Datum.

Kategorien: **Neu** (neue Funktionen), **Verbessert** (bestehendes Verhalten), **Behoben**
(Fehler), **Intern** (Struktur, Tooling, nicht sichtbar).

## Unveröffentlicht

### Neu
- Sonne/Mond-Knopf in der Kopfleiste: schaltet zwischen hellem und dunklem Design um. Die
  Wahl bleibt gespeichert; ohne eigene Wahl gilt weiter die Systemeinstellung.
- Bereich „Üben“ mit zwölf Übungen: ein virtueller Screenreader mit NVDA-Tasten
  (Überschriften, Orientierungspunkte, Formularfelder, Listen, Tabellen), ein
  Tastatur-Parcours, der Mausklicks nicht zählt, Fehlersuche mit dem Inspektor und ein Quiz
  „Was sagt der Screenreader?“. Gelöste Übungen werden markiert.
- ARIA-Kompass als eigene App: 22 Lektionen in sechs Kapiteln – Grundlagen, Struktur &
  Verstecken, Zustände, Live-Regionen, Widgets, Fokus & Tastatur. Jede mit Live-Beispiel,
  Attributtabelle, „So nicht – so“-Code, „Geht es ohne ARIA?“ und Angular-Hinweisen.
- Schalter „ARIA zeigen“: Etiketten an allen Rollen und `aria-*`-Attributen der Seite,
  live aktualisiert.
- Accessibility-Inspektor unter jedem Beispiel: Rolle, Accessible Name mit Quelle,
  Zustände, Beschreibung, NVDA-ähnliche Ansage und Warnungen; dazu eine Baumansicht.
- Referenz mit allen Attributen aus allen Lektionen, durchsuchbar.
- Zweisprachig (Deutsch/Englisch) mit Sprachlink oben rechts, Suche mit `Strg+K`,
  Lernfortschritt, hell und dunkel.

### Verbessert
- Neues App-Symbol im Stil der Schwester-App Daumenregel: dunkler Grund, blasse Linien und
  ein goldener Akzent – alle fünf Apps sehen jetzt im Tab wie eine Familie aus. Dazu
  `favicon.ico` für ältere Browser und ein Icon für den Homescreen (`apple-touch-icon.png`).
- Die Schwester-Apps HTML-Atlas und Angular-Patterns erscheinen als Kacheln auf der Startseite.
- Die Kachel zum CSS-Atlas nennt dessen neuen Umfang: über 100 Einträge.
- Die Schwester-Apps Daumenregel und CSS-Atlas erscheinen auf der Startseite als Kacheln mit
  Symbol für externe Links statt als Liste.

### Behoben
- Fachliche Durchsicht aller 22 Lektionen: unter anderem `role="presentation"` auf
  Containern, `title` und WCAG 1.4.13, Home/End beim CDK-`ListKeyManager` nur auf Wunsch,
  Angular-Material-Details und die Reihenfolge bei positivem `tabindex`.
- Inspektor: `<aside>` in `<main>` gilt wieder als `complementary`, eine unbestimmte
  `<progress>`-Leiste meldet keinen Wert „0“ mehr, Absätze werden mit ihrem Text statt als
  „paragraph“ angesagt, und `aria-describedby` berücksichtigt `aria-label` der Ziele.

### Intern
- `tools/make_icons.py` erzeugt SVG, ICO und PNG aus einer einzigen Geometrie (braucht
  Pillow).
