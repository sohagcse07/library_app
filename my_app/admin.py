from django.contrib import admin
from .models import Book , Author , Course , Student ,Profile

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Profile)


