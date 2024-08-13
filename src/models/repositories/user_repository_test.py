from unittest.mock import Mock
from .user_repository import UserRepository

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()

class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()

def test_registry_user():
    username = "John"
    password = "John123@"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.registry_user(username=username, password=password)

    cursor = mock_connection.cursor.return_value
    
    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)
    mock_connection.commit.assert_called_once()

def test_edit_balance():
    user_id = "1"
    new_balance = 234.1

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.edit_balance(user_id=user_id, new_balance=new_balance)

    cursor = mock_connection.cursor.return_value

    assert "UPDATE users" in cursor.execute.call_args[0][0]
    assert "SET balance = ?" in cursor.execute.call_args[0][0]
    assert "WHERE id = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (new_balance, user_id)
    mock_connection.commit.assert_called_once()

def test_get_user_by_username():
    username = "john"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.get_user_by_username(username=username)

    cursor = mock_connection.cursor.return_value

    assert "SELECT id, username, password" in cursor.execute.call_args[0][0]
    assert "FROM users" in cursor.execute.call_args[0][0]
    assert "WHERE username = ?" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username,)
    cursor.fetchone.assert_called_once()
