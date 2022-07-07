from sys import prefix
from rest_framework.routers import DefaultRouter
from task.api.views import TaskView


router_task = DefaultRouter()

router_task.register(
    prefix='taks', basename='taks', viewset=TaskView)
