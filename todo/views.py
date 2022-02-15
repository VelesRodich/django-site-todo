from time import timezone
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .forms import TodoForm
from .models import Todo
from django.utils import timezone

# Todo_Home


def todo_home(request):
    return render(request, 'todo/home.html')


# Auth

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('todo:currenttodos')
            except IntegrityError:
                return render(request, 'signupuser/signupuser.html', {'form': UserCreationForm(), 'error': 'Такой пользователь существует'})

        else:
            return render(request, 'signupuser/signupuser.html', {'form': UserCreationForm(), 'error': 'Пароли не совпали'})


def loginuser(request):

    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'Имя и пароль не совпадают'})
        else:
            login(request, user)
            todos = Todo.objects.filter(user=request.user)
            return render(request, 'todo/currenttodos.html', {'todos': todos})


def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('todo:home')


# Todo


def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos': todos})


def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('todo:currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(), 'error': 'Введено недопустимое значение'})


def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    form = TodoForm(instance=todo)
    return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})


def changetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/changetodo.html', {'todo': todo, 'form': form})
    else:
        try:
            
            form = TodoForm(request.POST, instance=todo)
            
            form.user = request.user #добавляем эту строчку и менять данные в базе можно будет только данному пользователю
            form.save()
            return redirect('todo:currenttodos')
        except ValueError:
                return render(request, 'todo/changetodo.html', {'form': form, 'error': 'Ошибка!!!'})
            
            
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('todo:currenttodos')
        
    
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:currenttodos')
    
    
    
        