from django.contrib import admin

# Register your models here.
from account.models import ConfirmCode

admin.site.register(ConfirmCode)