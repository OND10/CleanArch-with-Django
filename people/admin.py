from django.contrib import admin
from .models import Person, Engineering, Student, Subject, StudentSubject
from people import models as app_modles

admin.site.register(Person)
admin.site.register(Engineering)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(StudentSubject)
admin.site.register(app_modles.BookModel)
admin.site.register(app_modles.AuthorMoel)
admin.site.register(app_modles.Employee)

