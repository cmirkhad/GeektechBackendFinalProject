from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ConfirmCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4) #4350 nco.kg/confirm/4350
    valid_until = models.DateTimeField() #23.10.2021

    def __str__(self):
        return self.code