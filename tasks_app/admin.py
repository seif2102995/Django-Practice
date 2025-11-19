from django.contrib import admin
from .models import Employee, Task

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'position']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to', 'due_date']
    search_fields = ['title', 'description']