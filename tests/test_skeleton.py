# -*- coding: utf-8 -*-

import pytest
from local_baniya_bl.skeleton import fib

__author__ = "filopd, aakashnaik007"
__copyright__ = "GeeksTrio"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
