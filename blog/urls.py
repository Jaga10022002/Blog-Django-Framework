from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    # more urls
    # path("post/details",views.details,name="details"),
    # dynamic urls  if we need string we have to modify like <str:post_id>
    path("post/<str:post_id>",views.details,name="details"),
    path("new_url",views.new_url_view,name="new_url"),
    path("old_url",views.old_url_redirect,name="old_url")


]