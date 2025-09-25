from main import Kalkulagailua

def test_batu():
    kalku = Kalkulagailua()
    emaitza = kalku.batu(3, 5)
    assert emaitza == 8
