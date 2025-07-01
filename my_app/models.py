from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class CommonInfo ( models.Model):

#     created_at  = models.DateTimeField( auto_now_add=True)
#     update_at  = models.DateTimeField( auto_now=True)

#     class Mata:

#         abstract = True

# class Product ( CommonInfo): // inherite kora jay ar ki 
    
#     naem = models.CharField(max_length=199)

class Author(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book (models.Model):

    name = models.CharField(max_length=199)
    author = models.ForeignKey(Author , on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Profile ( models.Model):

    boi = models.CharField(max_length=199)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Course(models.Model):

    name = models.CharField(max_length=199)

    def __str__(self):
        return self.name

class Student (models.Model):

    name = models.CharField(max_length=199)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name