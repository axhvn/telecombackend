from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request: HttpRequest):
  if not request.user.is_authenticated:
    return render(request, 'home.html')
  return HttpResponse("you're not logged in")

def blog(request: HttpRequest):
  return render(request, 'blog.html')

def blog_details(request: HttpRequest):
  return render(request, 'blog-details.html')

def portfolio_details(request: HttpRequest):
  return render(request, 'portfolio-details.html')

def home(request: HttpRequest):
  return render(request, 'home.html')