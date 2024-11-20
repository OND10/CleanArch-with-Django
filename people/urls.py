from django.contrib import admin
from django.urls import path
from people import views


app_name = 'people'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('books/', views.BookView.as_view(), name= 'book_list'),
    path('csrf_token/', views.get_csrftoken, name='csrf_token'),
    path('apply-raise/<int:precentage>/', views.apply_raise, name='apply_raise'),
    path('books/get_by_id/<int:book_id>/', views.get_by_id, name='book_detail'),
]