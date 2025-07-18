from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializers
from rest_framework import viewsets

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    permission_classes = [IsAuthenticated]

