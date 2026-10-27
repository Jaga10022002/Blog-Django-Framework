from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # url default length 200
    img_url = models.URLField(null=True)
    # adding new field
    created_at = models.DateTimeField(auto_now_add=True)

#    magic method based on the model it will print the data we need titile 
    def __str__(self):
        return self.title


