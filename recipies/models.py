from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=600)
    subtitle = models.CharField(max_length=600)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='recipies')
    intro = models.CharField(max_length=600)
    steps = models.CharField(max_length=600)
    summary = models.CharField(max_length=600)
    # likes = models.JSONField(blank=True)
    # comments = models.JSONField(blank=True)

    def __string__(self):
        return self.title
