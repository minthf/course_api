from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('courses/', CoursesListView.as_view(), name='courses-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail')
]
