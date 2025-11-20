# CORRECTED IMPORTS - Fixed the warning import issue
from rest_framework import viewsets, status, filters  # Import filters from rest_framework
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EmployeeViewSet(viewsets.ModelViewSet):
 
   
    
    queryset = Employee.objects.all()
    
    
    serializer_class = EmployeeSerializer
    
    # Enable filtering capabilities for this API
    filter_backends = [filters.SearchFilter]  
    
    # Fields that can be searched using ?search=query parameter
    search_fields = ['first_name', 'last_name']

    
    # # Fields that can be used for sorting with ?ordering=field_name
    # ordering_fields = ['first_name', 'last_name', 'created_at']
    
    # # Default ordering when no specific order is requested
    # ordering = ['first_name']  # Alphabetical by first name by default


class TaskViewSet(viewsets.ModelViewSet):
 
    
    # Defines which database records this ViewSet works with
    queryset = Task.objects.all()
    
    # Specifies how to convert Task objects to/from JSON
    serializer_class = TaskSerializer
    
    # Enable filtering capabilities for this API
    filter_backends = [DjangoFilterBackend]

     # Default ordering when no specific order is requested
    ordering = ['-created_at']  # Newest tasks first by default

     # Example: /api/tasks/?is_completed=true
    filterset_fields = ['is_completed']

    
    # Fields for exact matching with DjangoFilterBackend
    # # Fields that can be searched using ?search=query parameter
    # search_fields = ['title', 'description']  # Tasks should search title/description
    # # Fields that can be used for sorting with ?ordering=field_name
    # ordering_fields = ['created_at', 'due_date', 'title']
    
   



    # # Custom action: Mark task as completed
    # @action(detail=True, methods=['post'])
    # def mark_completed(self, request, pk=None):
    #     """
    #     Custom API endpoint to mark a specific task as completed
    #     URL: /api/tasks/{id}/mark_completed/
    #     Method: POST
    #     """
    #     # Get the specific task object based on the ID in the URL
    #     task = self.get_object()
        
    #     # Update the task status to completed
    #     task.is_completed = True
    #     task.save()  # Save changes to database
        
    #     # Convert the updated task to JSON and return it
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)

