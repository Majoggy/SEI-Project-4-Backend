from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name