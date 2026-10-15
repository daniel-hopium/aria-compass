# ARIA-Kompass – WAI-ARIA zum Anfassen

22 Lektionen zu WAI-ARIA: Rollen, Namen, Zustände, Live-Regionen, Widgets und Fokus. Jede
Lektion hat ein Live-Beispiel, einen Accessibility-Inspektor, „So nicht – so“-Code und
Hinweise für Angular. Auf Deutsch und Englisch.

Online: https://daniel-hopium.github.io/aria-compass/

## Starten

`index.html` im Browser öffnen, per Doppelklick. Kein Build, kein Server, keine
Abhängigkeiten. Internet braucht es nur für die Google-Schriften.

## Inhalt

Sechs Kapitel:

| Kapitel | Lektionen |
|---|---|
| Grundlagen | Die Regeln von ARIA, Accessibility Tree, Accessible Name, `aria-describedby` |
| Struktur & Verstecken | Landmarks, Verstecken (`hidden`, `sr-only`, `aria-hidden`, `inert`), Gruppen |
| Zustände | `aria-expanded`, `aria-pressed`, `aria-current`, Formularzustände |
| Live-Regionen | `role="status"` und `role="alert"`, Ladezustände mit `aria-busy` |
| Widgets | Tabs, Dialog, Menü-Button, Combobox, Switch, Tooltip |
| Fokus & Tastatur | `tabindex`, `aria-activedescendant`, Fokusmanagement |

Jede Lektion ist gleich aufgebaut: die Regel, eine Tabelle der Attribute, das Live-Beispiel,
„So nicht – so“ als Code, „Geht es ohne ARIA?“ (natives HTML zuerst), Richtig/Falsch, „In
Angular“ mit Code und „Warum?“. Dazu kommt eine Referenz mit allen Attributen aus allen
Lektionen, durchsuchbar.

## Üben

Zwölf Übungen unter `#ueben`, der Fortschritt („gelöst“) bleibt im Browser gespeichert:

- **Virtueller Screenreader:** eine kleine Shop-Seite, durch die du wie mit NVDA im
  Lesemodus navigierst – `↓`/`↑`, `H` und `1`–`6` für Überschriften, `D` für
  Orientierungspunkte, `K`, `B`, `F`, `E`, `R`, `C`, `L`, `I`, `T`, `G`. Mit Sprachausgabe als
  Protokoll und Aufgaben, die sich selbst abhaken.
- **Tastatur-Parcours:** Skip-Link, Aufklapper, Radiogruppe, Tabs, Dialog und Menü-Button nur
  mit der Tastatur bedienen. Ein Mausklick setzt die Aufgabe zurück. Dazu „Finde die
  Tastaturfalle“.
- **Fehlersuche:** Formular und Produktkarte mit versteckten ARIA-Fehlern, mit dem Inspektor
  untersuchen und melden.
- **Was sagt der Screenreader?** Quiz zu Namen und Zuständen; die richtige Antwort rechnet die
  Engine live aus.

## Sehen, was der Screenreader sieht

- **ARIA zeigen** (Schalter oben): Jedes Element mit Rolle oder `aria-*`-Attribut bekommt
  ein Etikett – implizite Rollen aus dem HTML in Grau, explizite Attribute in Rosa,
  Warnungen in Rot. Das Etikett folgt Änderungen live, etwa wenn `aria-expanded` umspringt.
- **Accessibility-Inspektor** unter jedem Beispiel: Klick, Tab oder Maus auf ein Element
  zeigt Rolle (implizit oder explizit), Accessible Name samt Quelle, Beschreibung, Zustände,
  Position („2 von 3“) und ungefähr, was NVDA vorliest. In der Ansicht **Baum** steht der
  Accessibility Tree des ganzen Beispiels.

Die Berechnung ist eine vereinfachte Fassung von accname 1.2 und dem HTML-AAM – gut genug zum
Lernen, kein Ersatz für den Accessibility-Tab der Browser-Entwicklertools oder einen echten
Screenreader.

## Bedienung

- **Sprache:** Der Link oben rechts („English“ / „Deutsch“) wechselt die Sprache. Sie steht
  als `?lang=en` in der Adresse (teilbar), wird im `localStorage` gemerkt und folgt sonst der
  Browsersprache.
- `Strg+K` (Mac: `Cmd+K`) springt in die Suche der Seitenleiste.
- Jede Lektion hat eine eigene Adresse (`#tabs`); der Zurück-Button funktioniert.
- Lektionen lassen sich als gelernt markieren; der Stand bleibt im Browser.
- Hell und dunkel folgen der Systemeinstellung. Das Logo führt zur Startseite.

## Aufbau

Alles steckt in einer Datei:

- **`CHAPTERS`** und **`LESSONS`**: ein Objekt pro Lektion mit Regel, Attributtabelle
  (`attrs`), Beispiel-HTML (`demo`) und optional `init()` für das Verhalten, Code-Paaren
  (`bad`/`good`), Angular-Teil (`ng`, `ngCode`) und eigenem CSS mit der Lektions-ID als
  Präfix.
- **Engine**: `implicitRole()`, `accName()`, `accDesc()`, `accStates()` und `inspect()`
  berechnen, was im Accessibility Tree ankommt; `axTree()` baut den Baum.
- **Overlay und Inspektor**: ein `MutationObserver` zeichnet Etiketten und Inspektor neu,
  sobald sich im Beispiel ein Attribut ändert.
- **Zweisprachig:** `tx('Deutsch','English')` steht direkt neben jedem Text und liefert die
  Sprache des Seitenaufrufs. Code-Beispiele gibt es in beiden Sprachen, Angular-Code nur auf
  Englisch.

Teil einer Reihe mit dem [UI-Atlas](https://daniel-hopium.github.io/ui-atlas/), der
UI-Pattern-Library, dem [CSS-Atlas](https://daniel-hopium.github.io/css-atlas/), dem
[HTML-Atlas](https://daniel-hopium.github.io/html-atlas/) und
[Angular-Patterns](https://daniel-hopium.github.io/angular-patterns/). Die App-Hülle stammt aus dem UI-Atlas.
