def test_prozent_function__0_prozent_ungeügend():


# Arrange
testwert = 0;
soll_ergebnnis = 0;
# Act
ist_ergebnis = test_prozent_function(0);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__29_prozent_ungeügend():


# Arrange
testwert = 29;
soll_ergebnnis = 29;
# Act
ist_ergebnis = test_prozent_function(29);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__30_prozent_mangelhaft():


# Arrange
testwert = 30;
soll_ergebnnis = 30;
# Act
ist_ergebnis = test_prozent_function(30);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__49_prozent_mangelhaft():


# Arrange
testwert = 49;
soll_ergebnnis = 49;
# Act
ist_ergebnis = test_prozent_function(49);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__50_prozent_ausreichend():


# Arrange
testwert = 50;
soll_ergebnnis = 50;
# Act
ist_ergebnis = test_prozent_function(50);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__51_prozent_ausreichen():


# Arrange
testwert = 51;
soll_ergebnnis = 51;
# Act
ist_ergebnis = test_prozent_function(51);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__66_prozent_befriedigend():


# Arrange
testwert = 66;
soll_ergebnnis = 66;
# Act
ist_ergebnis = test_prozent_function(66);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__80_prozent_befriedigend():


# Arrange
testwert = 80;
soll_ergebnnis = 80;
# Act
ist_ergebnis = test_prozent_function(80);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__81_prozent_gut():


# Arrange
testwert = 81;
soll_ergebnnis = 81;
# Act
ist_ergebnis = test_prozent_function(81);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__91_prozent_gut():


# Arrange
testwert = 91;
soll_ergebnnis = 91;
# Act
ist_ergebnis = test_prozent_function(91);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__92_prozent_sehr_gut():


# Arrange
testwert = 92;
soll_ergebnnis = 92;
# Act
ist_ergebnis = test_prozent_function(92);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__100_prozent_sehr_gut():


# Arrange
testwert = 100;
soll_ergebnnis = 100;
# Act
ist_ergebnis = test_prozent_function(100);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__unterhalb_der_grenze():


# Arrange
testwert = -1;
soll_ergebnnis = ValueError;
# Act
ist_ergebnis = test_prozent_function(-1);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__oberhalb_der_grenze():


# Arrange
testwert = 101;
soll_ergebnnis = ValueError;
# Act
ist_ergebnis = test_prozent_function(101);
# Assert
assert ist_ergebnis == soll_ergebnnis;

def test_prozent_function__falsche_datentyp():


# Arrange
testwert = "test";
soll_ergebnnis = TypeError;
# Act
ist_ergebnis = test_prozent_function("test");
# Assert
assert ist_ergebnis == soll_ergebnnis;





