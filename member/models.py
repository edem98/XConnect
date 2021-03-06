from django.contrib.auth.models import User
from django.db import models


class Xmember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

