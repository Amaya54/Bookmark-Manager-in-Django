from django.db import models

# Create your models here.
class bookmark(models.Model):
	url = models.CharField(max_length = 255, primary_key = False)
	tag = models.CharField(max_length = 255, primary_key = False)