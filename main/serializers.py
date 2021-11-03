from rest_framework import serializers

from favorites.models import FavoriteNews, FavoriteLaw, FavoritePublication
from main.models import News, Law, Publication, ImageNews


class ImageNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = "image".split()


class NewsSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    images = ImageNewsSerializer(many=True)

    class Meta:
        model = News
        fields = "id image images title short_description full_description link is_main is_favorite".split()

    def get_is_favorite(self, news):
        request = self.context['request']
        print(request.user, news)
        return bool(request.user.is_authenticated and FavoriteNews.objects.filter(news=news, user=request.user))


class LawSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Law
        fields = 'id title short_description full_description file type is_favorite'.split()

    def get_is_favorite(self, law):
        request = self.context['request']
        print(request.user, law)
        return bool(request.user.is_authenticated and FavoriteLaw.objects.filter(law=law, user=request.user))


class PublicationSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = 'id title short_description full_description file type is_favorite'.split()

    def get_is_favorite(self, publication):
        request = self.context['request']
        print(request.user, publication)
        return bool(request.user.is_authenticated and FavoritePublication.objects.filter(publication=publication,
                                                                                         user=request.user))
