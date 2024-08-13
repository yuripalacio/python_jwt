from .password_handler import PasswordHandle

def test_encrypt():
    my_password = '123john'
    password_handler = PasswordHandle()

    hashed_password = password_handler.encrypt_password(password=my_password)

    password_checked = password_handler.check_password(
        password=my_password,
        hashed_password=hashed_password
    )

    assert password_checked
