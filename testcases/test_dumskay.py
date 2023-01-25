import pytest
from example1 import register_user as positive_register
from example_6 import register_user as empty_register
from example_16 import register_user as password_diff

def test_user_registration_positive():
    a = positive_register()
    assert a[0] == a[1]

def test_user_registration_all_empty():
    a = empty_register()
    assert a[0] == a[1]

def test_user_registration_password_diff():
    a = password_diff()
    assert a[0] == a[1]