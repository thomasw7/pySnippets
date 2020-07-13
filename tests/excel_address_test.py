import pytest
from excel_address import get_column_letters,get_column_number,get_rows_from_address,get_columns_from_address


@pytest.mark.parametrize('column_number, expected', [
    (13, 'M'),
    (40, 'AN'),
    (126, 'DV'),
    (16384, 'XFD')
])
def test_get_column_letters(column_number, expected):
    #

    #
    actual = get_column_letters(column_number)

    #
    assert actual == expected


@pytest.mark.parametrize('column_letters, expected', [
    ('M', 13),
    ('AN', 40),
    ('DV', 126),
    ('XFD', 16384)
])
def test_get_column_number(column_letters, expected):
    #

    #
    actual = get_column_number(column_letters)

    #
    assert actual == expected


@pytest.mark.parametrize('address, expected', [
    ('B2', [2]),
    ('B2:D5', [2,3,4,5]),
    ('B2:Z5,A11,Z10:Z15,B:D,3:5', [2,3,4,5,11,10,11,12,13,14,15,3,4,5]),
    ('B2:B2,Z2:B5,WOOT', [2,2,3,4,5])
])
def test_get_rows_from_address(address, expected):
    #

    #
    actual = get_rows_from_address(address)

    #
    assert actual == expected


@pytest.mark.parametrize('address, expected', [
    ('B2', [2]),
    ('B2:D5', [2,3,4]),
    ('B2:D5,A11,AD10:AF15,ZZ1:AAB1,B:D,3:5', [2,3,4,1,30,31,32,702,703,704,2,3,4]),
    ('B2:B2,D2:B5,WOOT', [2,2,3,4])
])
def test_get_columns_from_address(address, expected):
    #

    #
    actual = get_columns_from_address(address)

    #
    assert actual == expected

