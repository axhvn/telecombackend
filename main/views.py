from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *


# Create your views here.
def home(request: HttpRequest):
    if not request.user.is_authenticated:
        return render(request, "home.html")
    return HttpResponse("you're not logged in")


def blog(request: HttpRequest):
    return render(request, "blog.html")


def blog_details(request: HttpRequest):
    return render(request, "blog-details.html")


def portfolio_details(request: HttpRequest):
    return render(request, "portfolio-details.html")


def home(request: HttpRequest):
    news = News.objects.all()
    return render(request, "home.html", {"news": news})


def news_detail(request: HttpRequest, news_id: int):
    return render(request, "news_detail.html", {"new": News.objects.get(id=news_id)})
