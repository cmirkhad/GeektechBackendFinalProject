import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, ListAPIView, \
    ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from main.models import News, Law, Publication
from main.serializers import NewsSerializer, LawSerializer, PublicationSerializer, NewsCreateValidateSerializer, \
    LawCreateValidateSerializer, PublicationValidateCreateSerializer


class NewsListAPIView(ListCreateAPIView):
    pagination_class = PageNumberPagination

    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def post(self, request):
        form = request.data
        serializer = NewsCreateValidateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        link = form['link']
        News.objects.create(title=title,
                            short_description=short_description,
                            full_description=full_description,
                            publication_date=datetime.datetime.now(),
                            link=link)
        return Response(data={"Message": "News added"})


class LawListAPIView(ListAPIView):

    queryset = Law.objects.all()
    serializer_class = LawSerializer
    pagination_class = PageNumberPagination
    def post(self, request):
        form = request.data
        serializer = LawCreateValidateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        type = form['type']

        Law.objects.create(title=title,
                           short_description=short_description,
                           full_description=full_description,
                           publication_date=datetime.datetime.now(),
                           type=type

                           )
        return Response(data={"Message": "Law added"})


class PublicationListAPIView(ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        form = request.data
        serializer = PublicationValidateCreateSerializer(data=form)
        if not serializer.is_valid():
            return Response(
                data={'message': 'error',
                      'errors': serializer.errors},
                status=status.HTTP_406_NOT_ACCEPTABLE
            )
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        type = form['type']
        Publication.objects.create(title=title,
                                   short_description=short_description,
                                   full_description=full_description,
                                   publication_date=datetime.datetime.now(),
                                   type=type
                                   )
        return Response(data={"Message": "Publication added"})


class PublicationDetailAPIView(RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class NewsDetailAPIView(RetrieveAPIView):


    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LawDetailAPIView(RetrieveAPIView):
    queryset = Law.objects.all()
    serializer_class = LawSerializer
