from django.db import models


# Create your models here.
class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"Title: {self.title} | Description: {self.description}"
