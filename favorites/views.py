from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from favorites.models import FavoriteLaw, FavoritePublication, FavoriteNews
from favorites.serializers import FavoriteLawSerializer, FavoritePublicationSerializer, FavoriteNewsSerializer


class FavoriteLawListAPIView(APIView):
    def get(self, request):
        law = FavoriteLaw.objects.all()
        data = FavoriteLawSerializer(law, many = True, context={"request": request}).data
        return Response(data=data)


class FavoriteNewsListAPIView(APIView):
    def get(self, request):
        law = FavoriteNews.objects.all()
        data = FavoriteNewsSerializer(law, many = True, context={"request": request}).data
        return Response(data=data)


class FavoritePublicationListAPIView(APIView):

    def get(self, request):
        law = FavoritePublication.objects.all()
        data = FavoritePublicationSerializer(law, many = True, context={"request": request}).data
        return Response(data=data)

