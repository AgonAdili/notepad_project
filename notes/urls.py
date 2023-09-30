from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('notes/', views.note_list, name='note_list'),
    path('notes/<int:note_id>', views.view_note, name='view_note'),

    path('create/', views.create_note, name='create_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('chat/', views.chat_view, name='chat_view'),
]
