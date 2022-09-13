from django.db import models

# Create your models
 
 
 
               
class Formation(models.Model):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    phone = models.CharField(blank=False, max_length=255, verbose_name="phone")
    first_name  = models.CharField(blank=False, max_length=150, verbose_name="first_name")
    last_name  = models.CharField(blank=False, max_length=150, verbose_name="last_name")
    choices  = models.CharField(blank=False, max_length=650, verbose_name="choices")
 

    def __str__(self):
     return self.last_name
    
    

