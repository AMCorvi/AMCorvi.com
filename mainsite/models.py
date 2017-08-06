from django.db import models

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.name
