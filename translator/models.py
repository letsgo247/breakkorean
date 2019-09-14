from django.conf import settings
from django.db import models

class Inputs(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
