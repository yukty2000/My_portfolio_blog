from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
	email = models.EmailField(max_length=254)
	message = models.TextField()
	date_sent = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.email

# Create your models here.
