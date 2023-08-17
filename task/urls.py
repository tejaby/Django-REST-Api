# django

from django.urls import path, include

# routers

from .routers import router

urlpatterns = []

urlpatterns += router.urls
