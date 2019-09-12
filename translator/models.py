from django.conf import settings
from django.db import models
from django.utils import timezone

class Input(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


# Create your models here.
# 현재로서는 DB 필요성 못느끼므로 일단 패스!
