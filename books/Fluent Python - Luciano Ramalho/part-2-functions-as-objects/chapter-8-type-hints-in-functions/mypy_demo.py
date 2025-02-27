# pip install mypy
def show_count(count: int, singular: str, plural: str = '') -> str:
    if count == 1:
        return f"1 {singular}"
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'


# pytest
from pytest import mark


@mark.parametrize('qty, expected', [
    (1, '1 part'),
    (2, '2 parts'),
])
def test_show_count(qty, expected):
    got = show_count(qty, 'part')
    assert got == expected


def test_show_count_zero():
    got = show_count(0, 'part')
    assert got == 'no parts'


def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 children'
