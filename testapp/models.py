from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    town = models.CharField(max_length=30)

    def __str__(self):
        return self.name