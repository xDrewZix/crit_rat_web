from django.db import models

# Create your models here.

class Main(models.Model):
	"""The main page for critical rationalism"""
	titles = models.CharField(max_length=50)
	textmain = models.TextField()

	
	def __str__(self):
		return self.textmain
		return self.titles
		

class CritRats(models.Model):
	critrats = models.CharField(max_length=50)
	
	def __str__(self):
		return self.critrats