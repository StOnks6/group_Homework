import jwt
import datetime
import config
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

SECRET_KEY = config.JWT_KEY


def create_token(user_data):
    payload = {
        'user_data': user_data,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_data']
    except ExpiredSignatureError:
        return "Expired token"
    except InvalidTokenError:
        return "Invalid token"
    
user_data = {
    'user_id': 123,
    'username': 'example_user'
}


token = create_token(user_data)
print(token)

decoded_token = decode_token(token)
print(decoded_token)