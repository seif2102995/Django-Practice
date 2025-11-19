from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer

class EmployeeViewSet(viewsets.ModelViewSet):  #automatically provides: list, create, retrieve, update, partial_update, destroy
    queryset = Employee.objects.all()     #Defines which database records this ViewSet works with
    serializer_class = EmployeeSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
   