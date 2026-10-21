from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("HELLO WORLD YOU ARE AT BLOG INDEX!!")

# dynamic url here we have to pass another parameter post_id from urls.py
def details(request,post_id):
    return HttpResponse(f"This is the Post details Page. And ID is {post_id} ")