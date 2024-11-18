from django.contrib import admin
from django.urls import path
from people.Presentation import views


app_name = 'people'
urlpatterns = [
    path('books/', views.BookView.as_view(), name= 'book_list'),
    path('csrf_token/', views.get_csrftoken, name='csrf_token'),
    path('apply-raise/<int:precentage>/', views.apply_raise, name='apply_raise'),
]