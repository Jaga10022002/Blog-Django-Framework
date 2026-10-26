from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # url default length 200
    imageurl = models.URLField(blank=True)

#    magic method based on the model it will print the data we need titile 
    def __str__(self):
        return self.title
