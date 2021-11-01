import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import News, Law, Publication
from main.serializers import NewsSerializer, LawSerializer, PublicationSerializer


class NewsListAPIView(APIView):
    def get(self, request):
        news = News.objects.all()
        data = NewsSerializer(news, many=True, context={'request': request}).data
        return Response(data=data)

    def post(self, request):
        form = request.data
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


class LawListAPIView(APIView):
    def get(self, request):
        law = Law.objects.all()
        data = LawSerializer(law, many=True, context={"request": request}).data
        return Response(data=data)

    def post(self, request):
        form = request.data
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']
        type = form['type']

        Law.objects.create(title=title,
                           short_description=short_description,
                           full_description=full_description,
                           publication_date=datetime.datetime.now(),
                           type=type,

                           )
        return Response(data={"Message": "Law added"})


class PublicationListAPIView(APIView):
    permission_classes = ()

    def get(self, request):
        law = Publication.objects.all()
        data = PublicationSerializer(law, many=True, context={"request": request}).data
        return Response(data=data)

    def post(self, request):
        form = request.data
        title = form['title']
        short_description = form['short_description']
        full_description = form['full_description']

        Publication.objects.create(title=title,
                                   short_description=short_description,
                                   full_description=full_description,
                                   publication_date=datetime.datetime.now()
                                   )
        return Response(data={"Message": "Publication added"})


class PublicationDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class NewsDetailDeleteAPIView(RetrieveDestroyAPIView):

    permission_classes = (IsAuthenticated, )
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LawDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Law.objects.all()
    serializer_class = LawSerializer
