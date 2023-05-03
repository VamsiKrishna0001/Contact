from django.db import models

# Create your models here.


class management(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
