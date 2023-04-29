import pytest

from dynamic_programming.longest_common_subsequence import longest_common_subsequence


@pytest.mark.parametrize('str1, str2, expected', [
    ('GXTXAYB', 'AGGTAB', 'GTAB'),
    ('', '', ''),
    ('ABCD', 'A', 'A'),
])
def test_lcs(str1, str2, expected):
    actual = longest_common_subsequence(str1, str2)
    assert actual == expected

