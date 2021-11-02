from django.shortcuts import render
from .models import Task
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import TaskSerializer


# Create your views here.

@api_view(["GET"])
def test(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detaill/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
        }
    return Response(api_urls)




@api_view(["GET"])
def TaskViewSet(request):
    queryset = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(queryset, many = True)
    return Response(serializer.data)


@api_view(["GET"])
def TaskDetail(request, pk):
    queryset = Task.objects.get(id = pk)
    serializer = TaskSerializer(queryset, many = False)
    return Response(serializer.data)

@api_view(["POST"])
def TaskCreate(request):
    serializer = TaskSerializer(data = request.data)


    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(["POST"])
def TaskUpdate(request, pk):
    queryset = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=queryset, data = request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)


@api_view(["DELETE"])
def TaskDelete(request, id):
    queryset = Task.objects.get(id = id)
    queryset.delete()

    return Response("Successful deletion!!")