from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def home(request: HttpRequest):
  if not request.user.is_authenticated:
    return render(request, 'index.html')
  return HttpResponse("you're not logged in")