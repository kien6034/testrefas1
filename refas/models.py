from django.db import models

# Create your models here.
class Archive(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"