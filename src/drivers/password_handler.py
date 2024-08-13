import bcrypt

class PasswordHandle:
    def encrypt_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password=password.encode("utf-8"), salt=salt)

        return hashed_password

    def check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password=password.encode("utf-8"), hashed_password=hashed_password)