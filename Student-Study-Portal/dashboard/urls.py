from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('delete_note/<int:pk>', views.delete_note ,name="delete-note"),
    path('notes_details/<int:pk>', views.NotesDetailView.as_view() ,name="notes-details"),
    path('youtube',views.youtube,name="youtube"),
    path('homework',views.homework,name="homework"),
    path('update_homework/<int:pk>',views.update_homework,name="update-homework"),
    path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),
    path('todo', views.todo, name="todo"),
    path('update_todo/<int:pk>', views.update_todo, name="update-todo"),
    path('delete_todo/<int:pk>', views.delete_todo, name="delete-todo"),
    path('add_document/', views.add_document, name='add_document'),
    path('view_document/', views.view_document, name="view_document"),
    path('delete_document/<int:pk>', views.delete_document, name="delete_document"),
    path('add_document/', views.add_document, name='add_document'),
    path('view_document/', views.view_document, name="view_document"),
    path('delete_document/<int:pk>', views.delete_document, name="delete_document"),
    
]