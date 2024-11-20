from django.http import JsonResponse
from people.utils import decode_jwt

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(' ')[1]
            user = decode_jwt(token)
            if user:
                request.user = user
            else:
                return JsonResponse({'error': 'Invalid or fucking token'}, status=401)
        else:
            request.user = None

        return self.get_response(request)
