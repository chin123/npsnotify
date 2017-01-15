from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


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

#create new user tokens
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
