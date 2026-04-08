from django.shortcuts import render
from django.http import Http404
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