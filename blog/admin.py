from django.contrib import admin
from .models import Post,Category

# we can customize the admin interface also for that we are using class 
# now we have to register this model below the class becuase we modified the interface
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields =('title','content')
    list_filter = ('category','created_at')

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)