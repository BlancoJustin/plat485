import pytest
from plat485.projects.hw10.fruit_query import is_it_a_fruit

"""
Testable things:
Strings:
-In the list with correct syntax
-In list without correct syntax
    -typo
    -capitalization
    -punctuation/special character
-Not in list
-Other fruits (not in list fruits)

Lists:
-strings in fruits list
-strings not in fruits list

-Int testing
-Float testing



"""
def test_is_it_a_fruit_banana():
    assert is_it_a_fruit('banana') is True
def test_is_it_a_fruit_pear():
    assert is_it_a_fruit('pear') is True
def test_is_it_a_fruit_apple():
    assert is_it_a_fruit('apple') is True
def test_is_it_a_fruit_grape():
    assert is_it_a_fruit('grape') is True

def test_is_it_a_fruit_bananaa():
    assert is_it_a_fruit('bananaa') is False

def test_is_it_a_fruit_Banana():
    assert is_it_a_fruit('Banana') is False
def test_is_it_a_fruit_banana_char():
    assert is_it_a_fruit('banana!') is False

def test_is_it_a_fruit_orange():
    assert is_it_a_fruit('orange') is False

def test_is_it_a_fruit_straw():
    assert is_it_a_fruit('straw') is False

def test_is_it_a_fruit_strawberry():
    assert is_it_a_fruit('strawberry') is False


list1 = ['apple', 'pear']
def test_is_it_a_fruit_list_fruits():
    assert is_it_a_fruit(list1) is False

list2 = ['apple', 'orange', 'pear']
def test_is_it_a_fruit_list_some_fruits():
    assert is_it_a_fruit(list2) is False
list3 = ['straw','hat','car']
def test_is_it_a_fruit_list_not_fruit():
    assert is_it_a_fruit(list3) is False

def test_is_it_a_fruit_int():
    assert is_it_a_fruit(3) is False
def test_is_it_a_fruit_float():
    assert is_it_a_fruit(3.7) is False