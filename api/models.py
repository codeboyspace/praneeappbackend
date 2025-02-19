from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.username
