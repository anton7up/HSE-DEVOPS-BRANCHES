import pytest

from main.user import User
def test_register_new_user():
    user1 = User("1234", "Ivan", "Ivanov", "123@gmail.com", "2374bhwdh6G")
    assert user1.username == "1234"
    assert user1.name == "Ivan"
    assert user1.lastname == "Ivanov"

def test_register_new_user_fail():
    with pytest.raises(ValueError):
         User("1234", "Ivan", "Ivanov", "123@gmail.com", "12345678")

def test_get_username():
    user2 = User("1234", "Ivan", "Ivanov", "123@gmail.com", "2374bhwdh6G")
    assert user2.get_username() == "1234"
