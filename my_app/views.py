from django.shortcuts import render , HttpResponse 
from django.db.models import Count
from .models import Book , Student

# Create your views here.



def home ( request ):

    book = Book.objects.all() # 1 ta sql query 

    for i in book: # N sql query choltache 

        print( i.name , " " , i.author.name )
    # (n + 1) ta sql query lagtache and this is so bad for dev  so use 

    book = Book.objects.select_related('author') # single sql query coltache ,  JOIN  er kaj kore

    for i in book: # eta n porjonto normal loop colebe but ekta single babe kaj korbe 

        print ( i.name , " " , i.author.name)

    # lik 
    # SELECT BOOK.ID , BOOK.NAME , AUTHOR.ID , AUTHOR.NAME 
    # FROM BOOK 
    # INNER JOIN AUTHOR
    # ON BOOK.AUTHOR = AUTHOR.ID 

    students = Student.objects.all()

    for student in students:

        print( student.name , " " , [ i.name for i in student.course.all()])
    # N + 1 problem hoiya galo so use 

    students = Student.objects.prefetch_related('course') # many to many er jono prefetch use korte hoy 

    for student in students:

        print( student.name , " " , [ i.name for i in student.course.all()])


    # aggregate function 
    book = Book.objects.aggregate( total_book = Count('id'))
    print(book)


    # group by look like sql
    students = Student.objects.annotate(cours_count = Count('course')) 

    for student in students:

        print( student.name , " " , student.cours_count)
    

    # Order by 
    # book = Book.objects.order_by(('id')) // ASC
    book = Book.objects.order_by(('-id')) # DESC

    # advance query 
    book1 = Book.objects.filter(name__icontains = 'c++') # icontains dile lowecase e search kore 

    print (book1)

    # // sql --> derect hite kore tai time kom lage 
    # // orm --> sql --> database theke data niya ase tai ekto late hoy 


    return HttpResponse (  "hello world")

