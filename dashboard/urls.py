from django.urls import path
from .views import (
    DepartmentListCreateAPIView, DepartmentDetailAPIView,
    FacultyListCreateAPIView, FacultyDetailAPIView,
    TeacherListCreateAPIView, TeacherDetailAPIView,
    SubjectListCreateAPIView, SubjectDetailAPIView,
    GroupListCreateAPIView, GroupDetailAPIView,
    StudentListCreateAPIView, StudentDetailAPIView
)

urlpatterns = [
    # Department (Kafedra)
    path('departments/', DepartmentListCreateAPIView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentDetailAPIView.as_view(), name='department-detail'),

    # Faculty (Faculti)
    path('faculties/', FacultyListCreateAPIView.as_view(), name='faculty-list-create'),
    path('faculties/<int:pk>/', FacultyDetailAPIView.as_view(), name='faculty-detail'),

    # Teacher (O‘qituvchi)
    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),

    # Subject (Fan)
    path('subjects/', SubjectListCreateAPIView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailAPIView.as_view(), name='subject-detail'),

    # Group (Guruh)
    path('groups/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='group-detail'),

    # Student (Talaba)
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
]
