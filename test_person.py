from person import Person


def test_get_full_name():
    person = Person('George', 'Costanza', 5)
    assert person.get_full_name() == 'George Costanza'

def test_str():
    person = Person('Elaine', 'Benez', 5)
    assert str(person) == 'Elaine Benez'

def test_repr():
    george = Person(
        first_name='George',
        last_name='Costanza',
        height='5'
    )
    expected = """Person(first_name='George', last_name='Costanza', height='5')"""
    assert repr(george) == expected
