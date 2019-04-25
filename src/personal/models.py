from django.db import models

# Create your models here.
class person(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	age = models.DecimalField(decimal_places=2, max_digits=100)
	gender = models.CharField(max_length=20)
	featured = models.BooleanField(default=True)