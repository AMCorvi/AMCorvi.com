from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(min_length=30)
    url = models.URLField(max_length=50)
    description = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.name
