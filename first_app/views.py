from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article

def index(request):
    template = loader.get_template('index.html')
    articles = Article.objects.order_by('-created_at')[:5] #最新の5件を取得して created_atの新着順(頭の--がその意味)で並べ替え、aritclesに格納
    context = {
        'articles' : articles
    }
    return HttpResponse(template.render(context,request))

def page(request, page_id):
    message = 'ページ' + str(page_id)
    return HttpResponse(message)

def article(request,article_id):
    article = Article.objects.get(pk=article_id)
    template = loader.get_template('article.html')
    context = {
        'article' : article
    }
    return HttpResponse(template.render(context,request))