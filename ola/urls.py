from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.wName, name="wName") # <str:name> pega o nome que for inserido no url do site
]