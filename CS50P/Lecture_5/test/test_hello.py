from hello import hello

def test_defualt():
    assert hello() == "Hello, World"

def test_argument():
    assert hello("Pratheek") == "Hello, Pratheek"
