from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=129)
    originaltitle = models.CharField(null=True, blank=True, max_length=129)
    year = models.DateTimeField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)
    plot = models.TextField(null=True, blank=True)
    poster = models.ImageField(null=True, blank=True, upload_to='cars')
    landscape = models.ImageField(null=True, blank=True, upload_to='cars')
    movie_file = models.FileField(null=True, upload_to='uploads/')