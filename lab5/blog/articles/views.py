from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import Article


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
    else:
        return render(request, 'create_post.html', {})
    
    # Проверка обязательных полей
    if not (title and text):
        return render(request, 'create_post.html', {
            'form': {'title': title, 'text': text},
            'errors': 'Пожалуйста, заполните все поля!'
        })
    
    # Проверка существования статьи
    if Article.objects.filter(title=title).exists():
        return render(request, 'create_post.html', {
            'form': {'title': title, 'text': text},
            'errors': 'Статья с таким названием существует!'
        })
    
    # Создаем новую статью
    article = Article.objects.create(
        title=title,
        text=text,
        author=request.user
    )
    
    return redirect('get_article', article_id=article.id)