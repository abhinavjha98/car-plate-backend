import email
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from users.utils import get_tokens_for_user
# Create your views here.

class UserAuthView(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = ()

    def login(self, request):
            emailid = request.data.get('emailid')
            password = request.data.get('password')
            try:
                username = CustomUser.objects.get(email=emailid)
            except Exception:
                return Response(
                    data={'status': False, 'message': 'It seems that you have entered an incorrect Username'}, 
                    status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if user is None:
                return Response(
                    data={'status': False, 'message': 'It seems that you have entered an incorrect Username or Password'}, 
                    status=status.HTTP_400_BAD_REQUEST)
            else:
                token = get_tokens_for_user(user)
                return Response(
                    data={'status': True, 'message': 'Authentication successfull', 'token': token}, 
                    status=status.HTTP_200_OK)