from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests
# Create your views here.

# Token
mapbox_access_token = 'pk.eyJ1IjoiZXJib2xvbG8iLCJhIjoiY2xoYXE1dXRjMGs2cjNlcWZyZTN1dGpubCJ9.ebkHfOR-yJSeGoVk3dZ8vQ'

def index(request):
    raiting = Ratind.objects.all()
    news = News.objects.all()

    per_page = 12

    # Получаем первую фотографию под новостями
    first_image = []
    for post in news:
        img = PhotosNews.objects.filter(Gallery = post.Gallery).first()
        if img is None:
            error = True
        else:
            first_image.append(img.URL)
    
    current_page_news = Paginator(news, per_page=per_page)
    current_page_img = Paginator(first_image, per_page=per_page)
    
    page_num = current_page_news.num_pages
    try:
        page = request.GET.get("page", 1)
        news = current_page_news.page(page)
        page = request.GET.get("page", 1)
        images = current_page_img.page(page)

    except (PageNotAnInteger, TypeError):
        news = current_page_news.page(1)
        images = current_page_img.page(1)
        
    except EmptyPage:
        news = current_page_news.page(current_page_news.num_pages)
        images = current_page_img.page(current_page_img.num_pages)

    news_image_mixed = zip(news, images)
    context = {
        "raiting": raiting,
        "news":news,
        "news_image_mixed":news_image_mixed,
    }

    return render(request, 'index.html', context)

def news(request):
    list_of_news = News.objects.order_by('id')
    context = {
        'list_of_news': list_of_news
    }

    return render(request, 'pages/news_table.html', context)

def news_detail(request):

    context = {

    }

    return render(request, 'pages/news_detail.html', context)

def reviews(request):

    context = {

    }

    return render(request, 'pages/get_reviews.html', context)

def map(request):

    context = {

    }

    return render(request, 'pages/map.html', context)

def get_coordinates(address):
    print(f"Что получил: ",address)
    response = requests.get(f'https://api.mapbox.com/geocoding/v5/mapbox.places/{address}.json', params={
        'access_token': mapbox_access_token,
        'limit': 1
    })
    if response.status_code == 200:
        features = response.json()['features']
        print(f"Features: ", features)
        if features:
            coordinates = features[0]['center']
            print(f"Response: ", coordinates)
            return coordinates[::-1]  # Reverse coordinates to match the order (lat, lon)
    return None

def SearchInMap(request): 

    address = request.POST['regionname']
    add = address
    print(f"Address: ", address)
    coordinates = get_coordinates(address)
    print(f"Долгота: ", coordinates[0])
    print(f"Широта: ", coordinates[1])
    context = {
        'latitude': coordinates[0],
        'longitude': coordinates[1],
        'access_token': mapbox_access_token,
        'address': add,
    }
    return render(request,'pages/map copy.html',context)



def interactive(request):
    
    return render(request, 'pages/interactive.html')

def add_problem(request):
    
    context = {
        
    }
    return render(request, 'pages/problem_add.html', context)