from datetime import datetime, timedelta, timezone
import jwt
from src.configs.jwt_configs import jwt_infos

class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
        token = jwt.encode(
            payload={
              'exp': datetime.now(timezone.utc) + timedelta(hours=jwt_infos["JWT_EXP"]),
              **body
            },
            key=jwt_infos["JWT_KEY"],
            algorithm=jwt_infos["JWT_ALGORITHM"]
        )

        return token

    def decode_jwt_token(self, token: str) -> dict:
        token_information = jwt.decode(
            token, key="mykey", algorithms="HS256"
        )

        return token_information
