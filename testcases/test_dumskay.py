from example1 import register_user as positive_register
from example_6 import register_user as empty_register
from example_16 import register_user as password_diff
from example9_1 import register_user_without_email
from example13 import register_user_with_same_nick

def test_user_registration_positive():
    a = positive_register()
    assert a[0] == a[1]

def test_user_registration_all_empty():
    a = empty_register()
    assert a[0] == a[1]

def test_user_registration_password_diff():
    a = password_diff()
    assert a[0] == a[1]

def test_email_empty():
    a = register_user_without_email()
    assert a[0] == a[1]

def test_existing_user():
    a = register_user_with_same_nick()
    assert a[0] == a[1]