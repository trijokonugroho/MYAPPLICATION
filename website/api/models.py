from django.db import models
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    publised_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=250, blank=True)

    def save(self, *args, **kwargs):
        self.slug =slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}.{}".format(self.id, self.title)