# # from django.contrib.auth.models import User
# from django.http import request
# from .models import Task
# from .serializers import TaskSerializer
# from rest_framework import viewsets, serializers, routers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(["GET"])
# def TaskViewSet(request):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer(queryset, many = True)
#     return Response(serializer_class.data)



# router = routers.DefaultRouter()
# router.register(r'task',TaskViewSet)