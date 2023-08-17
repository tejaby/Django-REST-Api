# rest_framework

from rest_framework import routers

# viewsets

from .views import TaskViewset

router = routers.DefaultRouter()

router.register(r'api/task', TaskViewset)
