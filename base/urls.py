from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test', views.test),
    # path('getStudents', views.get_students),
    # path('deleteStudent/<int:student_id>/', views.delete_student, name='delete_student'),
    path('students', views.students),
    path('students/<int:id>',views.students),

]

