from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Article
from django.http import HttpResponse


# Create your views here.
def archive(request):
    posts = Article.objects.all().order_by('-created_date')
    
    return render(request=request, template_name='archive.html', context={'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        
        return render(request=request, template_name='article.html', context={'post': post})
    
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")

@login_required
def create_post(request):
    # Проверка HTTP-метода
    if request.method == "POST":
        # Объявляем переменные с данными для формы
        title = request.POST.get('title', '').strip()
        text = request.POST.get('text', '').strip()
        errors = []
        errors_text = ''
    else:
        return render(request=request, template_name='create_post.html', context={})
    
    # Проверка обязательных полей
    if not (title and text):
        errors.append('Пожалуйста, заполните все поля')
    
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