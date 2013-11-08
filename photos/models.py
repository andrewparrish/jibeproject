from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Photo(models.Model):
	name = models.CharField(max_length=200)
	picture = models.ImageField(upload_to="images/")

	def __unicode__(self):
		return self.name

