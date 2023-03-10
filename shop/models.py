from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    text = models.TextField()
    photo = models.ImageField(upload_to='images')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name
    
class Plan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name