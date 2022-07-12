from projects.api.serializer import ProjectSerializer
from projects.models import Project
from rest_framework.viewsets import ModelViewSet
from projects.api.permissions import IsAdminOrReadOnly


class ProjectsView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
