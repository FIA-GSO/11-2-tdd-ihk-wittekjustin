from notenberechnung import *

def test_prozent_function__0_prozent_ungeügend():

    # Arrange
    testwert = 0;
    soll_ergebnnis = 'ungenügend';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__29_prozent_ungeügend():

    # Arrange
    testwert = 29;
    soll_ergebnnis = 'ungenügend';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__30_prozent_mangelhaft():

    # Arrange
    testwert = 30;
    soll_ergebnnis = 'mangelhaft';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__49_prozent_mangelhaft():

    # Arrange
    testwert = 49;
    soll_ergebnnis = 'mangelhaft';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__50_prozent_ausreichend():

    # Arrange
    testwert = 50;
    soll_ergebnnis = 'ausreichend';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__51_prozent_ausreichen():

    # Arrange
    testwert = 51;
    soll_ergebnnis = 'ausreichend';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__66_prozent_ausreichend():

    # Arrange
    testwert = 66;
    soll_ergebnnis = 'ausreichend';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__80_prozent_befriedigend():

    # Arrange
    testwert = 80;
    soll_ergebnnis = 'befriedigend';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__81_prozent_gut():

    # Arrange
    testwert = 81;
    soll_ergebnnis = 'gut';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__91_prozent_gut():

    # Arrange
    testwert = 91;
    soll_ergebnnis = 'gut';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__92_prozent_sehr_gut():

    # Arrange
    testwert = 92;
    soll_ergebnnis = 'sehr gut';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__100_prozent_sehr_gut():

    # Arrange
    testwert = 100;
    soll_ergebnnis = 'sehr gut';
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__unterhalb_der_grenze():

    # Arrange
    testwert = -1;
    soll_ergebnnis = ValueError;
    # Act
    ist_ergebnis = prozent_function(-testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__oberhalb_der_grenze():

    # Arrange
    testwert = 101;
    soll_ergebnnis = ValueError;
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__falsche_datentyp():

    # Arrange
    testwert = "test";
    soll_ergebnnis = TypeError;
    # Act
    ist_ergebnis = prozent_function(testwert);
    # Assert
    assert ist_ergebnis == soll_ergebnnis;





