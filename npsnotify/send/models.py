from django.db import models
from django.utils import timezone

# Create your models here.
class notification(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    groups = models.TextField()
    goers = models.TextField()


    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class receipent(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    section = models.CharField(max_length=1)
    house = models.CharField(max_length=100)
