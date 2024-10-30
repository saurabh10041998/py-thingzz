from typing import Tuple


class VersionError(ValueError):
    ...

def parse_version(s: str) -> Tuple[int, int]:
    ret = tuple(int(x) for x in s.strip().split('.'))
    if len(ret) != 2:
        raise VersionError(f"expected #.# but got {s!r}")
    return ret

import pytest

@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        ("3.6", (3, 6)),
        ("2.7", (2, 7))
    )
)
def test_parse_version(input_s, expected):
    assert parse_version(input_s) == expected

def test_parse_version_not_a_number():
    with pytest.raises(ValueError):
        parse_version("3.a")

@pytest.mark.parametrize(
    ("input_s", "expected_err"),
    (
        ("3", "expected #.# but got '3'"),
        ("3.6.4", "expected #.# but got '3.6.4'")
    )
)
def test_parse_version_failure(input_s, expected_err):
    with pytest.raises(VersionError) as excinfo:
        parse_version(input_s)
    msg, = excinfo.value.args
    assert msg == expected_err
