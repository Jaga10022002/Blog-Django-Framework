from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any





class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args:Any,**option:Any):
        Category.objects.all().delete()
    
        categories = ['Sports',"Technology","Engineer","Medical","Food"]

        for categorie_name in categories:
            Category.objects.create(name = categorie_name)

        self.stdout.write(self.style.SUCCESS("Categories added Successfully"))