from django.db import models


# Create your models here.
class about(models.Model):

    def __str__(self):
        return self.name
