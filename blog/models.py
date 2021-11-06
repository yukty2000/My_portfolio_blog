from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	summary = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
