import pytest
from plat485.projects.hw11.sci_name import get_formal_name
from plat485.projects.hw11.sci_name import get_scientific_name

"""
Testable Things:
Testing a string in dictionary
Testing a string not in dictionary
Testing floats and ints (not in dictionary)
Testing list of fruits in dictionary
Testing empty string
"""

"""
Testing for initial method
"""
def test_get_formal_name_apple():
    formal_name = get_formal_name('apple')
    assert formal_name == 'Malus domestica'

def test_get_formal_name_vegetable():
    with pytest.raises(KeyError):
        formal_name = get_formal_name('carrot')

def test_get_formal_name_int():
    with pytest.raises(KeyError):
        formal_name = get_formal_name(12)

def test_get_formal_name_float():
    with pytest.raises(KeyError):
        formal_name = get_formal_name(1.2)

def test_get_formal_name_empty_string():
    with pytest.raises(KeyError):
        formal_name = get_formal_name('')

def test_get_formal_name_list_of_fruits():
    with pytest.raises(TypeError):
        fruits = ['mango', 'blueberry', 'cherry']
        formal_names = get_formal_name(fruits)


"""
Testing for new method
"""
def test_get_scientific_name_apple():
    scientific_name = get_scientific_name('apple')
    assert scientific_name == 'Malus domestica'

def test_get_scientific_name_vegetable():
    scientific_name = get_scientific_name('carrot')
    assert scientific_name == 'Unknown'

def test_get_scientific_name_int():
    scientific_name = get_scientific_name('12')
    assert scientific_name == 'Unknown'

def test_get_scientific_name_float():
    scientific_name = get_scientific_name(1.5)
    assert scientific_name == 'Unknown'

def test_get_scientific_name_empty_string():
    scientific_name = get_scientific_name('')
    assert scientific_name == 'Unknown'

def test_get_scientific_name_list_of_fruits():
    with pytest.raises(TypeError):
        fruits = ['mango', 'blueberry', 'cherry']
        scientific_names = get_formal_name(fruits)


"""
HW12 Parametrized Tests for HW11
"""


@pytest.mark.parametrize('fruit, expected_formal_name', [
    ('apple', 'Malus domestica'),
    ('banana', 'Musa acuminata'),
    ('orange', 'Citrus × sinensis'),
    ('strawberry', 'Fragaria × ananassa'),
    ('grape', 'Vitis vinifera'),
    ('pineapple', 'Ananas comosus'),
    ('mango', 'Mangifera indica'),
    ('blueberry', 'Vaccinium corymbosum'),
    ('peach', 'Prunus persica'),
    ('watermelon', 'Citrullus lanatus'),
    ('cherry', 'Prunus avium'),
    ('pear', 'Pyrus'),
    ('plum', 'Prunus domestica'),
    ('raspberry', 'Rubus idaeus'),
    ('kiwi', 'Actinidia deliciosa'),
    ('lemon', 'Citrus limon'),
    ('avocado', 'Persea americana'),
    ('pomegranate', 'Punica granatum'),
    ('cranberry', 'Vaccinium macrocarpon'),
    ('grapefruit', 'Citrus × paradisi')
])
def test_get_formal_name(fruit, expected_formal_name):
    result = get_formal_name(fruit)
    assert result == expected_formal_name

