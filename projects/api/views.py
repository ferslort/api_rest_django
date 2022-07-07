from projects.api.serializer import ProjectsSerializer
from projects.models import Project
from rest_framework.viewsets import ModelViewSet
from projects.api.permissions import IsAdminOrReadOnly


class ProjectsView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()
