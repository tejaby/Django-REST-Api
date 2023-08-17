# rest_framework

from rest_framework import viewsets, permissions

# serializers

from .serializers import TaskSerializer

# models

from .models import Task


class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]
