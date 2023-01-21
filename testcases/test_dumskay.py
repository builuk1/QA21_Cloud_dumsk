import pytest
from example1 import register_user


def test_user_registration():
    a = register_user()
    assert a[0] == a[1]