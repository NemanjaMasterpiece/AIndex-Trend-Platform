from celery import shared_task
from newspaper import Article
from .models import TrendArticle
import datetime
import random

@shared_task
def scrape_articles():
    keywords = ["AI", "machine learning", "deep learning", "neural networks"]
    urls = [
        'https://www.technologyreview.com/',
        'https://www.theverge.com/ai-artificial-intelligence',
        'https://techcrunch.com/category/artificial-intelligence/',
        'https://aimagazine.com/interviews/capgemini-ctio-reports-surge-in-enterprise-gen-ai-spend',
        'https://www.artificialintelligence-news.com/',
    ]
    
    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            
            if not article.title or not article.text:
                continue 
            if any(keyword.lower() in article.text.lower() for keyword in keywords):
                if not TrendArticle.objects.filter(title=article.title).exists():
                    trend_article = TrendArticle(
                        title=article.title,
                        content=article.text[:500],
                        link=url,
                        importance=random.randint(1, 10),
                        published_date=datetime.datetime.now()
                    )
                    trend_article.save()
        except Exception as e:
            print(f"Error processing {url}: {e}")
            continue