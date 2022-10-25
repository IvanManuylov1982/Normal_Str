import re
import pytest

from typing import List
from pydantic import BaseModel

#class Couple(BaseModel):
#    items: List[(str, int)]


def get_normal_str(sttr: str) -> str:
    """
    Нормализует строку

    :param str sttr: Не нормализованная строка
    :return: Нормализованная строка

    >>> get_normal_str('A1BB2C10D')
    'ABBBBCCCCCCCCCCD'
    >>> get_normal_str('')
    ''
    >>> get_normal_str('3A')
    'A'
    """

    normal_str: str = ''
#    norm_couple = Couple()
    norm_couple: List = re.findall(r'([A-Za-z]+)(\d*)', sttr)
    for couple in norm_couple:
        try:
            normal_str += couple[0] * int(couple[1])
        except ValueError:
            normal_str += couple[0]
    return normal_str


@pytest.mark.parametrize('test_input, expected', [
    ('B3A1', 'BBBA'),
    ('A1C4', 'ACCCC'),
    ('A', 'A'),
    ('A10', 'AAAAAAAAAA'),
    ('A1', 'A')
])
def test_get_str(test_input, expected):
    assert get_normal_str(test_input) == expected


if __name__ == "__main__":
    import doctest
    doctest.testmod()
