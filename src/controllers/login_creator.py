from src.models.interface.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandle

class LoginCreator:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandle()

    def create(self, username: str, password: str) -> dict:
        user = self.__find_user(username=username)
        user_id = user[0]
        hashed_password = user[2]

        self.__verify_correct_password(password=password, hashed_password=hashed_password)
        token = self.__create_jwt_token(user_id=user_id)

        return self.__format_response(username=username, token=token)

    def __find_user(self, username: str) -> tuple[int, str, str]:
        user = self.__user_repository.get_user_by_username(username=username)
        if not user: raise Exception("User not found")

        return user

    def __verify_correct_password(self, password: str, hashed_password: str) -> None:
        is_password_corret = self.__password_handler.check_password(
            password=password,
            hashed_password=hashed_password
        )
        if not is_password_corret: raise Exception("Wrong Password")

    def __create_jwt_token(self, user_id: int) -> str:
        payload = { "user_id": user_id }
        token = self.__jwt_handler.create_jwt_token(body=payload)

        return token

    def __format_response(self, username: str, token: str) -> dict:
        return {
            "access": True,
            "username": username,
            "token": token
        }
