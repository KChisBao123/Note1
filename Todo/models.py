from django.db import models
from django.utils import timezone

# Create your models here.
class Note(models.Model):
    Title = models.CharField(max_length=50)
    Detail = models.TextField()
    Date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.Title