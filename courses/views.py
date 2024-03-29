from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from .models import Course
from .serializers import CoursesListSerializer, CourseDetailSerializer


class CoursesListView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CoursesListSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CoursesListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
