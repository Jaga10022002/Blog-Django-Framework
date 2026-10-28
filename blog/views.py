from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.urls import reverse
import logging
from .models import Post


logger = logging.getLogger("Testing")

# need the post data for entire views we can paste it top like global data
# static demo data
# posts = [
#          {'id':1,'title':"Post 1",'content':'Content of Post 1'},
#          {'id':2,'title':"Post 2",'content':'Content of Post 2'},
#          {'id':3,'title':"Post 3",'content':'Content of Post 3'},
#          {'id':4,'title':"Post 4",'content':'Content of Post 4'},

#     ]

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    # getting data from post model
    posts = Post.objects.all()
    return render(request,'index.html',{'blog_tit': blog_title,'post_list':posts})
    # return HttpResponse("HELLO WORLD YOU ARE AT BLOG INDEX!!")

def details(request, slug):
 
    try:   
     post = Post.objects.get(slug = slug)
     related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
       raise Http404("Post doesn't exist")

    
    return render(request, 'details.html', {'post': post,'related_posts':related_posts})



# redirect
def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL")