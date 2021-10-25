from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from main.models import News, Law, Publication


class FavoriteNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FavoriteLaw(models.Model):
    law = models.ForeignKey(Law, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FavoritePublication(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
