from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('articles/', views.article_list, name='article_list'),  
    path('article/<int:id>/', views.article_detail, name='article_detail'), 
    path('podaci/', views.podaci, name="podaci"),
    path('update/', views.update_articles, name='update_articles'),
    path('update-one/', views.update_one_article, name='update_one_article'),  
]