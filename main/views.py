from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth.models import User


# Create your views here.
def home(request: HttpRequest):
    if not request.user.is_authenticated:
        return render(request, "home.html")
    return HttpResponse("you're not logged in")


def blog(request: HttpRequest):
    blogs = Blog.objects.all().order_by("-created_at")[:6]
    return render(request, "blog.html", {"blogs": blogs})


def blog_details(request: HttpRequest, blog_id: int):
    return render(
        request,
        "blog-details.html",
        {
            "blog": Blog.objects.get(id=blog_id),
            "blogs": Blog.objects.all().order_by("-created_at")[:6],
        },
    )


# def portfolio_details(request: HttpRequest):
#     return render(request, "portfolio-details.html")


def home(request: HttpRequest):
    news = News.objects.all().order_by("-created_at")[:3]
    return render(request, "home.html", {"news": news})


def news_detail(request: HttpRequest, news_id: int):
    return render(request, "news_detail.html", {"new": News.objects.get(id=news_id)})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            return render(
                request,
                "login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return render(request, "login.html")


def register_view(request):
    if request.method == "POST":
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensuring password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
        except:
            return render(
                request, "register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return redirect("home")
    else:
        return render(request, "register.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        Feedback.objects.create(
            name=name, email=email, subject=subject, message=message
        )
    return redirect("home")

def telecomwifi(request: HttpRequest):
    return render(request, "telecomwifi.html")

def internet_cafe(request: HttpRequest):
    return render(request, "internet_cafe.html")

def tariffs(request: HttpRequest):
    return render(request, "tariffs.html")

def hosting(request: HttpRequest):
    return render(request, "hosting.html")

def hosting_virtual(request: HttpRequest):
    return render(request, "hosting_virtual.html")
def hosting_physical(request: HttpRequest):
    return render(request, "hosting_physical.html")


# def blog(request):
