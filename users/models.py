from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
 
YEAR_CHOICES = [('1er année', '1er année'),
                ('2ème année', '2ème année'),
                ('3ème année', '3ème année'),
                ('4ème année', '4ème année'),
                ('5ème année', '5ème année')]
CELL_CHOICES = [('media', 'media'),
                ('contact & sponsoring', 'contact & sponsoring'),
                ('Events', 'Events'),
                ('Gaming', 'Gaming'),
                ('Formation', 'Formation')]

DAY_CHOICES =[ ('Premier jour', 'Premier jour'),
               ('Deuxième jour', 'Deuxième jour'),]
               
class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    phone = models.CharField(blank=False, max_length=255, verbose_name="phone")
    first_name  = models.CharField(blank=False, max_length=150, verbose_name="first_name")
    last_name  = models.CharField(blank=False, max_length=150, verbose_name="last_name")
    year = models.CharField( max_length=500, choices=YEAR_CHOICES, default='1er année')
    cell = models.CharField( max_length=500, choices=CELL_CHOICES, default='media')
    day = models.CharField( max_length=500, choices=DAY_CHOICES, default='Premier jour')
    psw  = models.CharField(blank=False, max_length=350, verbose_name="psw")

    def __str__(self):
     return self.last_name
    
    

