from django.db import models
from django.utils import timezone


class Shoe(models.Model):
    author = models.ForeignKey('auth.User')
    brand = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    counter = models.BigIntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def create(self):
        self.save()

    def __str__(self):
        return self.name