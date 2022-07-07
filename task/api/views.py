from task.api.serializer import TaskSerializer
from task.models import Task
from rest_framework.viewsets import ModelViewSet
from projects.api.permissions import IsAdminOrReadOnly


class TaskView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
