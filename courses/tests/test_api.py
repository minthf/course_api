from rest_framework.test import APITestCase
from django.urls import reverse
from courses.models import Category, Course

class CoursesListApiTestCase(APITestCase):

    def test_get(self):
        url = reverse('courses-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_without_course(self):
        url = reverse('courses-list')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 400)

    def test_post_with_course(self):
        data = {
            "name": "English",
            "description": "eng courses",
            "category": {
                "name": "Languages",
                "imgpath": "123"
                },
            "logo": "123",
            "contacts": [
                {
                    "type": 1,
                    "value": "123123123"
                }
            ],
            "branches": [
                {
                    "latitude": "123",
                    "longitude": "123",
                    "address": "123"
                }
            ]
        }
        url = reverse('courses-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

class CourseDetailApiTestCase(APITestCase):

    def test_get_without_course(self):
        url = reverse('course-detail', args=[1,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_get_200_with_course(self):
        Category.objects.create(name='Languages', imgpath='123')
        Course.objects.create(name='English', description='English courses', category=Category.objects.get(id=1), logo='123')
        url = reverse('course-detail', args=[1,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_with_course(self):
        Category.objects.create(name='Languages', imgpath='123')
        Course.objects.create(name='English', description='English courses', category=Category.objects.get(id=1), logo='123')
        url = reverse('course-detail', args=[1,])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_delete_without_course(self):
        url = reverse('course-detail', args=[1,])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 404)