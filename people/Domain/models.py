from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Engineering(models.Model):
    
    person = models.ForeignKey(Person, on_delete= models.CASCADE)
    description = models.TextField()    
    

class Student(models.Model):
    name = models.CharField(max_length= 36)

    def __str__(self):
        return str(self.pk)

class Subject(models.Model):
    name = models.CharField(max_length= 36)

    def __str__(self):
        return str(self.pk)
    
class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    enrollment_date  = models.DateField()

    def __str__(self):
        return f"{self.student.name} enrolled in {self.subject.name}"


class BookModel(models.Model):
    title = models.CharField(max_length= 255)
    author = models.CharField(max_length= 255)
    published_date = models.DateField()
    pin = models.CharField(max_length= 50)
    
    def __str__(self):
        return self.title

class AuthorMoel(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=40)
    salary = models.FloatField()
    
    def __str__(self):
        return self.name


# def students():
#     return Student.objects.all()


# def subjects():
#     return Subject.objects.all()


# def student_subject_list(request):
#       return render(request, 'school/student_subject_list.html', context = {'students':students(), 'subjects':subjects()}) 