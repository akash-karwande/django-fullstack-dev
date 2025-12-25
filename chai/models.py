from django.db import models
from django.utils import timezone

# Create your models here.

chai_types = [
    ("ML", "MASALA"),
    ("GL", "GINGER"),
    ("PL", "PLAIN"),
    ("LE", "LEMAN"),
    ]

class ChaiVarities(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chais/')
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chai_types, default='ML')



def __str__(self):
    return self.name
