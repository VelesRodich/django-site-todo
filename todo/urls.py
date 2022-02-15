
from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
  
    path('', views.todo_home, name='home'),
    
       
    #Todos 
    path('current/', views.currenttodos, name='currenttodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('view/<int:todo_pk>/', views.viewtodo, name='viewtodo'),
    path('change/<int:todo_pk>/', views.changetodo, name='changetodo'), 
    path('complete/<int:todo_pk>/', views.completetodo, name='completetodo'),
    path('delete/<int:todo_pk>/', views.deletetodo, name='deletetodo'),
     
    
]