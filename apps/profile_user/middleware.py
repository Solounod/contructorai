from django.utils.deprecation import MiddlewareMixin
from .models import Hammer
from django.http import JsonResponse
import uuid


class AnonHammerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.perfil = request.user.profile.hammer
        else:
            token = request.COOKIES.get('anon_hammer_token')
            if token:
                try:
                    hammer = Hammer.objects.get(token=token)
                except Hammer.DoesNotExist:
                    hammer = Hammer.objects.create()
            else:
                hammer = Hammer.objects.create()
            request.hammer = hammer
            request.new_hammer = not token


    def process_response(self, request, response):
        if hasattr(request, 'new_hammer') and request.new_hammer:
            response.set_cookie('anon_hammer_token', request.hammer.token, max_age=60*60*24)
        return response
        