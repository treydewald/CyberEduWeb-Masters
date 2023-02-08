from django.db import models

# Create your models here.
class Video(models.Model):
    cat = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pos = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Article(models.Model):
    cat = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pos = models.CharField(max_length=200)

    def __str__(self):
        return self.title
