from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden
from ..Domain.models import Person, Engineering, Student, Subject, StudentSubject
# from ..forms import PersonForm, EngineeringForm, StudentSubjectForm 
from django.urls import reverse
from people.Domain import models as app_models
import json
from django.middleware.csrf import get_token
from django.views import View
from people.Application.Services.BookService import BookService
from people.Infrastructure.Repositories.BookRepository import BookRepository
from people.Application.DTOs.BookDto import BookDto
from django.views.decorators.csrf import ensure_csrf_cookie



from django.core import serializers
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def index(requst):

    return render(requst, 'index.html')




@ensure_csrf_cookie
def get_csrftoken(request):
    
    token = get_token(request)
    return JsonResponse({
        'csrfToken':token
    })

class BookView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = BookService(BookRepository())

    def get(self, request):
        books = self.service.get_all_books()
        books_data = [book.__dict__ for book in books]
        return JsonResponse({'data': books_data, 'message': 'Get All Books Successfully', 'status': 200})

    def post(self, request):
        data = json.loads(request.body)
        book_dto = BookDto(**data)
        added_book = self.service.add_book(book_dto)
        
        return JsonResponse({'data': added_book.__dict__, 'message': 'Book added successfully', 'status': 201})



def apply_raise(request, precentage : int):
    
    try:
        
        multiplier = 1 + (precentage/100)
        employees = app_models.Employee.objects.all()
        
        for employee in employees:
            employee.salary = multiplier
            employee.save()
    
        return JsonResponse({'status': 'success', 'message': f'Salaries increased by {precentage}%.'})
    
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})    

def getAll(request):
    result = Person.objects.all()

    return render(request, 'getAll.html', context= {'result' : result})

# def create(request):
#     if request.method == "POST":
#         person_form = PersonForm(data=request.POST, files=request.FILES)

#         if person_form.is_valid():
#             person_form.save()  # Save the form directly, including image
#             return HttpResponseRedirect(reverse('people:getAll'))  # Ensure 'basic_app:getAll' matches your namespace and URL name
#         else:
#             print('Something went wrong during creation')
#     else:
#         person_form = PersonForm()
        
#     return render(request, 'create.html', context={'person_form': person_form})


def create_engineering(request):
    
    if request.method == "POST":
        form = EngineeringForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('people:view_engineerings'))
    else:
        form = EngineeringForm()
    return render(request, 'create_engineering.html', {'form': form})

def view_engineerings(request):
    engineerings = Engineering.objects.all()
    return render(request, 'view_engineerings.html', {'engineerings': engineerings})


def students():
    return Student.objects.all()

def subjects():
    return Subject.objects.all()

def student_subject_list(request):
    student_subjects = StudentSubject.objects.all()
    return render(request, 'student_subject_list.html', {
        'student_subjects': student_subjects
    })

def student_subject_create(request):
    # Get all students and subjects to pass as choices
    student_choices = [(student.id, student.name) for student in students()]
    subject_choices = [(subject.id, subject.name) for subject in subjects()]

    if request.method == 'POST':
        form = StudentSubjectForm(request.POST)
        form.fields['student'].choices = student_choices
        form.fields['subject'].choices = subject_choices

        if form.is_valid():
            # Retrieve the IDs and ensure they are integers

            print(str(form.cleaned_data['student']))
            print(str(form.cleaned_data['subject']))
            
            student_id = form.cleaned_data['student']
            subject_id = form.cleaned_data['subject']
            enrollment_date = form.cleaned_data['enrollment_date']

            # student_id[stud]

            # Fetch the actual Student and Subject instances based on their IDs
            student = Student.objects.get(id=student_id[''])
            subject = Subject.objects.get(id=subject_id)

            # Create the StudentSubject with valid objects
            StudentSubject.objects.create(student=student, subject=subject, enrollment_date=enrollment_date)

            return HttpResponseRedirect(reverse('people:student_subject_list'))
    else:
        # Initialize form with choices
        form = StudentSubjectForm()
        form.fields['student'].choices = student_choices
        form.fields['subject'].choices = subject_choices

    return render(request, 'student_subject_form.html', {'form': form})


#  Views for Book Model

def get_books(request):
    if request.method == 'GET':
        books = list(app_models.Book.objects.values())
        return JsonResponse(books, safe = False)
    

def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = app_models.Book.objects.create(
            title = data['title'],
            author = data['author'],
             pin = data['pin'],
            published_date = data['published_date']
        )
        return JsonResponse({
            'id':book.id,
            'title':book.title,
            'author':book.author,
            'pin': str(book.pin),
            'published_date':str(book.published_date)
        }, status = 201)
    else:
        # Return a 405 Method Not Allowed for non-POST requests
        return HttpResponseForbidden("Method not allowed")


    
# def get_bookById(request, id):
#     if request.method == 'GET':
#         book = serializers.serialize(app_models.Book.objects.get())    

                         