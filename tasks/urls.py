from django.urls import path
from . import views


urlpatterns = [
    path('', views.test, name = "api"),
    path('task-list/', views.TaskViewSet, name = "task-list"),
    path('task-detail/<str:id>/', views.TaskDetail, name = "task-detail"),
    path('task-create/', views.TaskCreate, name = "task-create"),
    path('task-update/<str:id>/', views.TaskUpdate, name = "task-update"),
    path('task-delete/<str:id>/', views.TaskDelete, name = "task-delete"),
]