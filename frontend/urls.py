from django.urls import path
from . import views

urlpatterns = [
    path('', views.inedx, name = "views_todo_lists"),
]