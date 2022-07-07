from sys import prefix
from rest_framework.routers import DefaultRouter
from projects.api.views import ProjectsView


router_projects = DefaultRouter()

router_projects.register(
    prefix='projects', basename='projects', viewset=ProjectsView)
