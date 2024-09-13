from django.contrib import admin
from .models import Department, Faculty, Teacher, Subject, Group, Student

# Register models to the admin panel
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    search_fields = ['name']
    list_filter = ['department']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'department']
    search_fields = ['first_name', 'last_name']
    list_filter = ['department']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher']
    search_fields = ['name']
    list_filter = ['teacher']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty']
    search_fields = ['name']
    list_filter = ['faculty']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'group']
    search_fields = ['first_name', 'last_name']
    list_filter = ['group']
