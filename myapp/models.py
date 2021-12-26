from django.db import models
from django.db.models.base import Model

class Mobile(models.Model):
    Brand_Name = models.CharField(max_length=50, blank=False , null=False)
    Model = models.CharField(max_length=50, blank=False , null=False )
    Color = models.CharField(max_length=50,  blank=False , null=False)
    JAN_Code = models.CharField(max_length=50, blank= False, null=False)
    
    def __str__(self):
        return self.Brand_Name +" "+ self.Model
    