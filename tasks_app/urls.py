from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

# Register our ViewSets with the router
router.register(r'employees', views.EmployeeViewSet)
router.register(r'tasks', views.TaskViewSet)

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
]