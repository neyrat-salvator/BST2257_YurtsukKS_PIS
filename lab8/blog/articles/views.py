from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Article
from django.http import HttpResponse
import re


# Create your views here.
def archive(request):
    current_user = request.user
    current_user_id = current_user.id

    if current_user.is_superuser:
        posts = Article.objects.all().order_by('-created_date')
    else:
        posts = Article.objects.filter(author=current_user_id).order_by('-created_date')
    
    return render(request=request, template_name='archive.html', context={'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        
        return render(request=request, template_name='article.html', context={'post': post})
    
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")

def create_post(request):
    # Проверка HTTP-метода
    if request.method == "POST":
        # Объявляем переменные с данными для формы
        title = request.POST.get('title', '').strip()
        text = request.POST.get('text', '').strip()
        errors = []
    else:
        return render(request=request, template_name='create_post.html', context={})
    
    # Проверка обязательных полей
    if not title:
        errors.append('Пожалуйста, заполните полt title')
    if not text:
        errors.append('Пожалуйста, заполните поле text')
    
    # Проверка существования статьи
    if Article.objects.filter(title=title).exists():
        errors.append('Статья с таким названием существует')
    
    # Проверка на количество символов
    if len(text) < 10:
        errors.append('Текст должен содержать минимум 10 символов')
    
    if len(errors) > 0:
        for error_index, error_value in enumerate(iterable=errors, start=1):
            errors[error_index-1] = f'{error_index}: {error_value}'
        return render(request=request, template_name='create_post.html', context={
            'form': {'title': title, 'text': text},
            'errors': errors
        })
    
    # Создаем новую статью
    article = Article.objects.create(
        title=title,
        text=text,
        author=request.user
    )
    
    return redirect('get_article', article_id=article.id)

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password_confirm = request.POST.get('password_confirm', '').strip()
        incorrect_symbols = [' ', ' ']
        email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        username_pattern = r'^[a-zA-Z0-9_-]+$'
        errors = []
    else:
        return render(request=request, template_name='registration.html', context={})
    
    # Проверка пустых полей
    if not username:
        errors.append('Пожалуйста, заполните полt username')
    if not email:
        errors.append('Пожалуйста, заполните полt email')
    if not password:
        errors.append('Пожалуйста, заполните полt password')
    
    # Проверка условий полей
    if len(username) < 2 or len(username) > 150:
        errors.append('Имя пользователя должно быть от 2 до 150 символов')
    if not (re.match(username_pattern, username)):
        errors.append('Имя пользователя может содержать только латинские буквы, цифры и следующие символы: "-", "_"')
    if not (re.match(email_pattern, email)):
        errors.append('Адрес электронной почты должен быть в формате mailid@maildomen.domen')
    if len(password) < 8:
        errors.append('Пароль должен содержать не меньше 8 символов')
    if any([symb in password for symb in incorrect_symbols]):
        errors.append('Пароль не должен содержать пробелы')
    
    # Проверка совпадения паролей
    if password != password_confirm:
        errors.append('Пароли не совпадают')
    
    # Проверка существования пользователя
    username_check = User.objects.filter(username=username).exists()
    email_check = User.objects.filter(email=email).exists()
    if username_check:
        errors.append('Пользователь с таким логином уже существует')
    if email_check:
        errors.append('Пользователь с таким адресом почты уже существует')
        
    if len(errors) > 0:
        for error_index, error_value in enumerate(iterable=errors, start=1):
            errors[error_index-1] = f'{error_index}: {error_value}'
        return render(request=request, template_name='registration.html', context={
            'form': {'username': username, 'email': email},
            'errors': errors
        })
    
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )
    
    login(request, user)
    return redirect('archive')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        errors = []
    else:
        return render(request=request, template_name='login.html', context={})
    
    if not username:
        errors.append('Пожалуйста, заполните полt username')
    if not password:
        errors.append('Пожалуйста, заполните полt password')
        
    user = authenticate(request=request, username=username, password=password)
    
    if user is None:
        errors.append('Неверное имя пользователя или пароль')
        
    if len(errors) > 0:
        for error_index, error_value in enumerate(iterable=errors, start=1):
            errors[error_index-1] = f'{error_index}: {error_value}'
        return render(request=request, template_name='login.html', context={
            'form': {'username': username},
            'errors': errors
        })
    
    login(request=request, user=user)
    next_url = request.GET.get('next', 'archive')
    
    return redirect(next_url)

def logout_view(request):
    logout(request)
    
    return redirect('archive')