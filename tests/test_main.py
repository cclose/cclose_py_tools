#!/usr/bin/env python3

# import pytest
import hello_python.main as hpm


def test_foo():
    assert 'foo' != 'bar'


def test_say_hi():
    assert hpm.say_hi('Bob') == 'Hello, Bob!'
