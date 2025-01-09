from django.urls import path
from .views import add_hobby

urlpatterns = [
    path("add/", add_hobby, name="add_hobby"),
]
