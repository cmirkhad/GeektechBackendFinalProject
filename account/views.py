import datetime
import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from account.models import ConfirmCode


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(
            username=username,
            email="a@n.ru",
            password=password,
            is_active=False
        )
        code = str(random.randint(1000, 9999))
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=20)
        ConfirmCode.objects.create(user=user, code=code, valid_until=valid_until)
        # send_code_to_phone(code, username)
        return Response(data={'message': "User created!!!!!1"})


class ConfirmAPIView(APIView):
    def post(self, request):
        code = request.data['code']
        code_list = ConfirmCode.objects.filter(code=code,
                                               valid_until__gte=datetime.datetime.now()
                                               )
        print("hello ")
        if code_list:

            confirmcode = code_list[0]
            confirmcode.user.is_active = True
            confirmcode.user.save()


            code_list.delete()
            return Response(data={'message': 'user activated'})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LoginAPIView(APIView):
    def post(request):

        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={
                'token': token.key
            })
        else:
            return Response(data={
                'message': "User not found"
            }, status=status.HTTP_404_NOT_FOUND)
