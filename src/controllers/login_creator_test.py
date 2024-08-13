import pytest
from src.drivers.password_handler import PasswordHandle
from .login_creator import LoginCreator

MOCK_USERNAME = "myUsername"
MOCK_PASSWORD = "myPassword"
MOCK_HASHED_PASSWORD = PasswordHandle().encrypt_password(password=MOCK_PASSWORD)

class MockUserRepository:
    def get_user_by_username(self, username):
        return (10, username, MOCK_HASHED_PASSWORD)

def test_create():
    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username=MOCK_USERNAME, password=MOCK_PASSWORD)

    assert response["access"]
    assert response["username"] == MOCK_USERNAME
    assert response["token"] is not None

def test_create_with_wrong_password():
    login_creator = LoginCreator(MockUserRepository())

    with pytest.raises(Exception):
        login_creator.create(username=MOCK_USERNAME, password="wrong_password")
