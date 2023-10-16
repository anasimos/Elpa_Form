from django.db import models

# Create your models here.
class Reading(models.Model):
    
    
    reading_id =models.AutoField(primary_key=True)
    BPNumber= models.IntegerField()
    fullname=models.CharField(max_length=50)
    accNumber=models.IntegerField()
    meterReading=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.fullname