from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

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


class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Archiver','Archiver'),
        ('Client','Client')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Client')
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Custom related_name to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related_name to avoid conflicts
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    def __str__(self):
        return self.username


# def students():
#     return Student.objects.all()


# def subjects():
#     return Subject.objects.all()


# def student_subject_list(request):
#       return render(request, 'school/student_subject_list.html', context = {'students':students(), 'subjects':subjects()}) 