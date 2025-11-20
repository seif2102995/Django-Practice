from django.db import models



class Employee(models.Model):
  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
 
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True) #1st creation only and never changes
    updated_at = models.DateTimeField(auto_now=True) # changes on every update 
    
    # tostring method
    def __str__(self):   
        return f"{self.first_name} {self.last_name} - {self.position}"
    
    # gives options 
    class Meta:
        ordering = ['-created_at']  
       
        

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)  

    assigned_to = models.ForeignKey(
        'Employee',
        on_delete=models.CASCADE,
        related_name='tasks', # instead of task_set (emp.task_set)->(emp.tasks) .......... how the other model refers back to this one. emp->tasks
        null=True,
        blank=True,
    ) # null -> DB level ..... blank ->app level (form validation)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {'Completed' if self.is_completed else 'Pending'}"

    class Meta:
        ordering = ['-created_at']