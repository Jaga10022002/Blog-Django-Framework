from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    return render(request,'index.html',{'blog_tit': blog_title})
    # return HttpResponse("HELLO WORLD YOU ARE AT BLOG INDEX!!")

# dynamic url here we have to pass another parameter post_id from urls.py
def details(request,post_id):
        return render(request,'details.html')
    # return HttpResponse(f"This is the Post details Page. And ID is {post_id} ")

# redirect
def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL")