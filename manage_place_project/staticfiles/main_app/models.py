from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name