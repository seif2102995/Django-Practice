from rest_framework import serializers
from .models import Employee, Task

class EmployeeSerializer(serializers.ModelSerializer):
   
    tasks_count = serializers.SerializerMethodField() #This creates a READ-ONLY field that's calculated by a method ... doesnt exist in db
    
    class Meta:
        model = Employee
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'position',
            
            'tasks_count',  # Custom field we added
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def get_tasks_count(self, obj):
        
        return obj.tasks.count()  
    


class TaskSerializer(serializers.ModelSerializer):

    assigned_to_name = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    

