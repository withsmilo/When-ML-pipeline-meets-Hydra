# -*- coding: utf-8 -*-

import pytest
from when_ml_pipeline_meets_hydra.skeleton import fib

__author__ = "Sungjun, Kim"
__copyright__ = "Sungjun, Kim"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
