from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Name', max_length=64)
    imgpath = models.CharField(verbose_name='ImagePath', max_length=64)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(verbose_name='Name', max_length=64)
    description = models.CharField(verbose_name='Description', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    logo = models.CharField(verbose_name='Logo', max_length=64)

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude = models.CharField(verbose_name='Latitude', max_length=64)
    longitude = models.CharField(verbose_name='Longitude', max_length=64)
    address = models.CharField(verbose_name='Address', max_length=64)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    def __str__(self):
        return self.address

class Contact(models.Model):
    CONTACTS = [
        (1, 'PHONE'),
        (2, 'EMAIL'),
        (3, 'FACEBOOK')
    ]
    type = models.IntegerField(choices=CONTACTS, default=1)
    value = models.CharField(verbose_name='Value', max_length=64)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.value

