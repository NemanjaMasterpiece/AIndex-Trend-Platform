from django.shortcuts import render, get_object_or_404, redirect
from .models import TrendArticle
from django.db.models import Q
from newspaper import Article
from django.utils import timezone
import random 
from django.http import HttpResponse
from django.http import JsonResponse
from .tasks import scrape_articles
from django.urls import get_resolver

def index(request):
    articles = TrendArticle.objects.order_by('-importance')[:3]
    return render(request, 'index.html', {'articles': articles})

def article_list(request):
    query = request.GET.get('q', '')
    filter_type = request.GET.get('filter_type', 'latest')
    articles = TrendArticle.objects.all()

    if query:
        exact_article = TrendArticle.objects.filter(title__iexact=query).first() 
        if exact_article:
            return redirect('article_detail', id=exact_article.id) 
        articles = articles.filter(Q(title__icontains=query) | Q(content__icontains=query))

    if filter_type == 'latest':
        articles = articles.order_by('-published_date')
    elif filter_type == 'important':
        articles = articles.order_by('-importance')
    return render(request, 'articles/article_list.html', {'articles': articles, 'query': query, 'filter_type': filter_type})

def article_detail(request, id):
    article = get_object_or_404(TrendArticle, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})


# Ovo je za automatsko postavljanje, tasks.py
"""
def update_articles(request):
    if request.method == 'POST':
        scrape_articles.delay()  # Pokreće task u pozadini
        return redirect('article_list')
"""
# Ovo je za automatsko postavljanje takođe

def update_articles(request):    
    if request.method == 'POST':
        urls = [
            'https://www.theverge.com/news/637542/chatgpt-says-our-gpus-are-melting-as-it-puts-limit-on-image-generation-requests'
            #'https://www.theverge.com/ai-artificial-intelligence',
            #'https://techcrunch.com/category/artificial-intelligence/',
            #'https://aimagazine.com/',
            #'https://www.artificialintelligence-news.com/',
        ]
        for url in urls:
            article = Article(url)
            article.download()
            article.parse()

            if not TrendArticle.objects.filter(title=article.title).exists():
                trend_article = TrendArticle(
                    title=article.title,
                    content=article.text[:500],
                    link=url,
                    importance=random.randint(1, 10),
                    published_date=timezone.now()
                )
                trend_article.save()
        return redirect('article_list')
    return HttpResponse("Nema novih članaka.") 
""""""

article_urls = [
    'https://www.artificialintelligence-news.com/news/uk-and-singapore-form-alliance-guide-ai-in-finance/',
    'https://www.theverge.com/news/646308/openai-countersues-elon-musk',
    'https://www.theverge.com/news/637542/chatgpt-says-our-gpus-are-melting-as-it-puts-limit-on-image-generation-requests',
    'https://techcrunch.com/2025/04/01/chatgpt-isnt-the-only-chatbot-thats-gaining-users/',
    'https://www.artificialintelligence-news.com/news/amazon-nova-act-step-towards-smarter-web-native-ai-agents/'
]

def update_one_article(request):
    if request.method == 'POST':
        if not article_urls:
            return JsonResponse({"message": "Nema više članaka za dodavanje."}, status=200)
        
        url = article_urls.pop(0)
        article = Article(url)
        article.download()
        article.parse()

        if not TrendArticle.objects.filter(title=article.title).exists():
            trend_article = TrendArticle(
                title=article.title,
                content=article.text[:500],
                link=url,
                importance=random.randint(1, 10),
                published_date=timezone.now()
            )
            trend_article.save()
            return JsonResponse({"message": "Članak dodat!", "title": article.title}, status=200)
        return JsonResponse({"message": "Članak već postoji."}, status=200)
    return JsonResponse({"error": "Neispravan zahtev"}, status=400)

def podaci(request):
    return render(request, "podaci.html")