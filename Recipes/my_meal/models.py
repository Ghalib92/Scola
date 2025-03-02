from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')  # Stores images in /media/blog_images/

    def __str__(self):
        return self.title
