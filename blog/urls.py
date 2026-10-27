from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("",views.index, name="index"),
    # more urls
    # path("post/details",views.details,name="details"),
    # dynamic urls  if we need string we have to modify like <str:post_id>
    path("post/<str:slug>",views.details,name="details"),
    path("new_something_url",views.new_url_view,name="new_page_url"),
    path("old_url",views.old_url_redirect,name="old_url")


]