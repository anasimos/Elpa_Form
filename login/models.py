from django.db import models

# Create your models here.
class Auth(models.Model):
    
    
    username =models.CharField(primary_key=True,max_length=50)
    password =models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.username