from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Fernando', 'Cardozo') == 'Cardozo, Fernando'
    assert make_full_name('John', 'Lennon') == 'Lennon, John'
    assert make_full_name('Paul', 'McCartney') == 'McCartney, Paul'
    assert make_full_name('George', 'Harrison') == 'Harrison, George'
    assert make_full_name('Ringo', 'Starr') == 'Starr, Ringo'


def test_extract_family_name():
    assert extract_family_name('Cardozo; Fernando') == 'Cardozo'
    assert extract_family_name('Lennon; John') == 'Lennon'
    assert extract_family_name('McCartney; Paul') == 'McCartney'
    assert extract_family_name('Harrison; George') == 'Harrison'
    assert extract_family_name('Starr; Ringo') == 'Starr'

def test_extract_given_name():
    assert extract_given_name('Fernando; Cardozo') == 'Fernando'
    assert extract_given_name('John; Lennon') == 'John'
    assert extract_given_name('Paul; McCartney') == 'Paul'
    assert extract_given_name('George; Harrison') == 'George'
    assert extract_given_name('Ringo; Starr') == 'Ringo'


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
