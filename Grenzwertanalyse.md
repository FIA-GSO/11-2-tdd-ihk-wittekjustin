# Grenzwertanalyse
Tipp: benutzen Sie einen [Tabellengenerator für Markdown](https://www.tablesgenerator.com/markdown_tables)

## Muster
### Name der Funktion
| # | parameter_1 | ...  | parameter_n  | erwartetes Ergebnis      |
|---|-------------|------|--------------|--------------------------|
| 1 | wert        | wert | wert         | Ergebnis  oder Exception |
| 2 | 0           | 0    | ungenügend   | 0 Prozent                |
| 3 | 29          |      | ungenügend   | 29 Prozent               |
| 3 | 30          |      | mangelhaft   | 30 Prozent               |
| 3 | 49          |      | mangelhaft   | 49 Prozent               |
| 3 | 50          |      | ausreichend  | 50 Prozent               |
| 3 | 66          |      | ausreichend  | 66 Prozent               |
| 3 | 67          |      | befriedigend | 67 Prozent               |
| 3 | 80          |      | befriedigend | 80 Prozent               |
| 3 | 81          |      | gut          | 81 Prozent               |
| 3 | 91          |      | gut          | 91 Prozent               |
| 3 | 92          |      | sehr gut     | 92 Prozent               |
| 3 | 100         |      | sehr gut     | 100 Prozent              |
| 3 | -1          |      | ValueError   | ValueError               |
| 3 | 101         |      | ValueError   | ValueError               |
| 3 | "text"      |      | ValueError   | TYPEERROR                |

| 3 | 1      |  100 |    | TYPEERROR                |
| 3 | 2      |    1 | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |
| 3 | "text"      |      | ValueError   | TYPEERROR                |





# Arrange
testwert = 0;
soll_ergebnnis = 0;
# Act
ist_ergebnis = test_prozent_function(0);
# Assert
assert ist_ergebnis == soll_ergebnnis;
