import Bottle4
def test_webapp_index():
    assert Bottle4.index() == 'Hi!'