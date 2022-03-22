from django.db import models

# Create your models here.
class Todo(models.Model):
    reminder=models.CharField(max_length=200)
    priority=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.reminder