from .jwt_handler import JwtHandler

def test_jwt_handler():
    jwt_hander = JwtHandler()
    body = {
        "username": "johndoe",
        "where": "i'm here",
        "mail": "johndoe@python.com"
    }

    token = jwt_hander.create_jwt_token(body=body)
    token_informations = jwt_hander.decode_jwt_token(token)

    assert token is not None
    assert isinstance(token, str)
    assert token_informations["username"] == body["username"]
    assert token_informations["where"] == body["where"]
    assert token_informations["mail"] == body["mail"]
