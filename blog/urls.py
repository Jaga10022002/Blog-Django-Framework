from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    # more urls
    # path("post/details",views.details,name="details"),
    # dynamic urls
    path("post/<int:post_id>",views.details,name="details")


]