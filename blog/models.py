from django.db import models
from django.utils.text import slugify

# Create your models here.

# category
class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # url default length 200
    img_url = models.URLField(null=True)
    # adding new field
    created_at = models.DateTimeField(auto_now_add=True)
    # slug filesd
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def save(self,*args,**kwasrgs):
        # need to genrate unique value based on the tiltle
        self.slug = slugify(self.title)
        super().save(*args,**kwasrgs)

#    magic method based on the model it will print the data we need titile 
    def __str__(self):
        return self.title

class AboutUs(models.Model):
    content = models.TextField()