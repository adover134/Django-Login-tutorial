import requests
from rest_framework import viewsets

from auth.models import User
from auth.serializers import UserSerializer

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def logout_view(request):
    client_id = settings.SOCIAL_AUTH_KAKAO_KEY
    logout_redirect_url = settings.LOGOUT_REDIRECT_URL

    kakao_logout_url = (
        f"https://kauth.kakao.com/oauth/logout?"
        f"client_id={client_id}&logout_redirect_uri={logout_redirect_url}"
    )
    logout(request)
    return redirect(kakao_logout_url)
