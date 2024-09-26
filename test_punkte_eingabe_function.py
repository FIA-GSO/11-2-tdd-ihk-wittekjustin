def test_punkte_eingabe_function__maximale_punktzahl():

    # Arrange
    punkte = 100;
    gesamtpunkte = 100;
    soll_ergebnnis = 100;
    # Act
    ist_ergebnis = punkte_eingabe_function(punkte / gesamtpunkte * 100);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;
def test_prozent_function__falsche_datentyp():
    # Arrange
    punkte = 0;
    gesamtpunkte = 100;
    soll_ergebnnis = 0;
    # Act
    ist_ergebnis = punkte_eingabe_function(punkte / gesamtpunkte * 100);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;
def test_prozent_function__falsche_datentyp():

    # Arrange
    punkte = -1;
    gesamtpunkte = 100;
    soll_ergebnnis = ValueError;
    # Act
    ist_ergebnis = punkte_eingabe_function(punkte / gesamtpunkte * 100);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;
def test_prozent_function__falsche_datentyp():

    # Arrange
    punkte = 101;
    gesamtpunkte = 100;
    soll_ergebnnis = ValueError;
    # Act
    ist_ergebnis = punkte_eingabe_function(punkte / gesamtpunkte * 100);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;
def test_prozent_function__falsche_datentyp():

    # Arrange
    punkte = '50';
    gesamtpunkte = 100;
    soll_ergebnnis = TypeError;
    # Act
    ist_ergebnis = punkte_eingabe_function(punkte / gesamtpunkte * 100);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;
def test_prozent_function__falsche_datentyp():
    # Arrange
    punkte = 100;
    gesamtpunkte = '100';
    soll_ergebnnis = 100;
    # Act
    ist_ergebnis = punkte_eingabe_function(punkte / gesamtpunkte * 100);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;
