from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Book(models.Model):
    ISBN = models.CharField(primary_key = True, max_length=50)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishDate = models.DateField(default=timezone.now)
    
    #TODO
    def __str__(self):
        return self.title
    

def tenDays():
        return timezone.now() + timezone.timedelta(days=10)
    
class Booking(models.Model):
    bookedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    bookedBook = models.ForeignKey(Book, on_delete=models.CASCADE)
    returnDate = models.DateField(default=tenDays)
    
    class Meta:
        unique_together = (
            ('bookedBy', 'bookedBook'),
        )

    def __str__(self):
        return str(self.bookedBy) + str(self.bookedBook)
