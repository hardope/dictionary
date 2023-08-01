from django.db import models

# Create your models here.
class Word(models.Model):
     word = models.CharField(max_length=200)
     word_length = models.IntegerField(default=0)
     word_class = models.CharField(max_length=200)
     definition = models.TextField()
     
     def __str__(self):
          return self.word
