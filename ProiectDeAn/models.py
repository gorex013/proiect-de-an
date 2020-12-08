from django.db import models
from django.contrib.auth.models import User


class Angajat(models.Model):
    user_id = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    alternate_phone_number = models.CharField('phone number', max_length=10, null=True)

    def __init__(self):
        super().__init__()
        User.objects.get(id=self.user_id).is_staff = True


class Client(models.Model):
    user_id = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    alternate_phone_number = models.CharField('phone number', max_length=10, null=True)

    def __init__(self):
        super().__init__()
        User.objects.get(id=self.user_id).is_staff = False
