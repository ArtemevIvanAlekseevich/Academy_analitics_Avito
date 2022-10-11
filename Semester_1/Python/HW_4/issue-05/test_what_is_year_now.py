import os

import pytest
from unittest.mock import patch

from what_is_year_now import what_is_year_now


def test_date_YMD():
    with patch("what_is_year_now.urllib.request.urlopen") as urlopen:
        current_dir = os.path.dirname(__file__)
        data = os.path.join(current_dir, 'date_YMD.json')
        urlopen.return_value = open(data, 'r')
        assert what_is_year_now() == 2019
        urlopen.assert_called_once()


def test_date_DMY():
    with patch("what_is_year_now.urllib.request.urlopen") as urlopen:
        current_dir = os.path.dirname(__file__)
        data = os.path.join(current_dir, 'date_DMY.json')
        urlopen.return_value = open(data, 'r')
        assert what_is_year_now() == 2022
        urlopen.assert_called_once()


def test_date_invalid():
    with patch("what_is_year_now.urllib.request.urlopen") as urlopen:
        current_dir = os.path.dirname(__file__)
        data = os.path.join(current_dir, 'date_invalid.json')
        urlopen.return_value = open(data, 'r')
        exception = ValueError
        with pytest.raises(exception):
            what_is_year_now()


def test_date_API():
    assert what_is_year_now() == 2022


if __name__ == '__main__':
    pytest.main(['issue-05/test_what_is_year_now.py',
                 '-v', '--cov=what_is_year_now'])
