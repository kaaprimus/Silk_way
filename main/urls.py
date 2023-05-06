from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('news-detail', views.news_detail, name='get_detail'),
    path('news', views.news, name='newses'),
    path('reviews', views.reviews, name='get_reviews'),
    path('map', views.map, name='get_map'),
    path('map/more-info', views.SearchInMap, name='map-more-info'),
    path('map_info', views.SearchInMap, name='mapinfo'),
    path('interactive/', views.interactive, name='interactive'),
    path('problem_add/', views.add_problem, name='problemadd')
]