from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)
    team = models.CharField(max_length=200)

    def __str__(self):
        return self.username
    

class Powerup(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_added = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title