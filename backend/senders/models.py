from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class notification(models.Model):
	message = models.CharField(max_length=400)
	author = models.ForeignKey('sender')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.message[:20] + "..."

class sender(models.Model):
	name = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

class recepient(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	house = models.CharField(max_length=20)
	grade = models.PositiveIntegerField()
	section = models.CharField(max_length=1)
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name + " " + str(self.grade) + " " + self.section
