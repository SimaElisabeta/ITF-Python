import pytest
from sesiunea8.app.func import is_div_3_5, only_ints, NotIntegerNumberException


# var1
def test_is_div_3_5_example():
    assert is_div_3_5(25) == 5


# var2 cu functia parametrizata
@pytest.mark.parametrize('n, expected', [
    (45, 35),
    (9, 3),
    (10, 5),
    (19, None)
])
def test_is_div_3_5(n, expected):
    assert is_div_3_5(n) == expected


@pytest.mark.parametrize('numbers', [
    [1, 3, 8, 1.54, 9, 13],
    ['545456454', 'salutari'],
    [1 + 2j, 7]
])
def test_only_ints(numbers):
    # ca sa testam ca se arunca o exceptie nu mai folosim assert ca la celelalte exemple
    # ci folosim formatul de jos: with pytest.raises(exceptia ce dorim sa o arunce)!
    with pytest.raises(NotIntegerNumberException):
        only_ints(numbers)
