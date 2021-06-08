from rest_framework import serializers
from .models import Course, Contact, Branch, Category

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = ('course', 'id')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ('course', 'id')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id',)


class CoursesListSerializer(serializers.ModelSerializer):
    contacts= ContactSerializer(many=True)
    branches = BranchSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ['name', 'description', 'category', 'logo', 'contacts', 'branches']


    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        category_data = validated_data.pop('category')

        category = Category.objects.get_or_create(**category_data)
        course = Course.objects.create(category = category[0], **validated_data)

        for contact_data in contacts_data:
            Contact.objects.create(course=course, **contact_data)

        for branch_data in branches_data:
            Branch.objects.create(course=course, **branch_data)
        return course

class CourseDetailSerializer(serializers.ModelSerializer):
    contacts= ContactSerializer(many=True, read_only=True)
    branches = BranchSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'description', 'category', 'logo', 'contacts', 'branches']
