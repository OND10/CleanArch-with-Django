import jwt
from django.contrib.auth import get_user_model
from django.conf import settings

# Get the actual user model
User = get_user_model()

def create_jwt(user):
    payload = {'id': user.id, 'username': user.username, 'role': user.role}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def decode_jwt(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return User.objects.get(id=payload['id'])
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
        return None
