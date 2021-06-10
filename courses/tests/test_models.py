from django.test import TestCase

from courses.models import Category, Course, Branch, Contact

class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Languages', imgpath='123')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length,64)

    def test_img_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('imgpath').max_length
        self.assertEquals(max_length,64)

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.name
        self.assertEquals(expected_object_name,str(category))
    

class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Languages', imgpath='123')
        Course.objects.create(name='English', description='English courses', category=Category.objects.get(id=1), logo='123')

    def test_name_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('name').max_length
        self.assertEquals(max_length,64)

    def test_description_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('description').max_length
        self.assertEquals(max_length,200)

    def test_logo_max_length(self):
        course = Course.objects.get(id=1)
        max_length = course._meta.get_field('logo').max_length
        self.assertEquals(max_length,64)

    def test_object_name_is_name(self):
        course = Course.objects.get(id=1)
        expected_object_name = course.name
        self.assertEquals(expected_object_name,str(course))

class BranchModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Languages', imgpath='123')
        Course.objects.create(name='English', description='English courses', category=Category.objects.get(id=1), logo='123')
        Branch.objects.create(latitude='123', longitude='321', address='Bishkek', course=Course.objects.get(id=1))

    def test_latitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('latitude').max_length
        self.assertEquals(max_length,64)

    def test_longitude_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('longitude').max_length
        self.assertEquals(max_length,64)

    def test_address_max_length(self):
        branch = Branch.objects.get(id=1)
        max_length = branch._meta.get_field('address').max_length
        self.assertEquals(max_length,64)

    def test_object_name_is_address(self):
        branch = Branch.objects.get(id=1)
        expected_object_name = branch.address
        self.assertEquals(expected_object_name,str(branch))

class ContactModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Languages', imgpath='123')
        Course.objects.create(name='English', description='English courses', category=Category.objects.get(id=1), logo='123')
        Contact.objects.create(type='123', value='321', course=Course.objects.get(id=1))

    def test_value_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('value').max_length
        self.assertEquals(max_length,64)

    def test_object_name_is_value(self):
        contact = Contact.objects.get(id=1)
        expected_object_name = contact.value
        self.assertEquals(expected_object_name,str(contact))

