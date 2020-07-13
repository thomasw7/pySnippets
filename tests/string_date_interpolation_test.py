import pytest
from datetime import datetime
from string_date_interpolation import interpolate

@pytest.mark.parametrize('interpolationKey, dt_string, rawString, expected', [
    ('date', '20200522 150122', 'path/to/nowhere-{date:%Y}/{date:%Y%m%d}', 'path/to/nowhere-2020/20200522'),
    ('date', '20200522 150122', 'path/to/nowhere-{date:%Y%m%d %H%M%S}', 'path/to/nowhere-20200522 150122'),
    ('key', '20200522 150122', 'path/to/nowhere-{date:%Y%m%d}', 'path/to/nowhere-{date:%Y%m%d}')
])
def test_interpolate(interpolationKey, dt_string, rawString, expected):
    #
    dt = datetime.strptime(dt_string, '%Y%m%d %H%M%S')

    #
    actual = interpolate(interpolationKey, dt, rawString)

    #
    assert actual == expected