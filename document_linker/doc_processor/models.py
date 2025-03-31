from django.db import models

class Keyword(models.Model):
    word = models.CharField(max_length=255)
    alternative_names= models.CharField(max_length=255)
    notation = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    reference = models.CharField(max_length=255)

    def __str__(self):
        return self.word
    
