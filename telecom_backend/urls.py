"""
URL configuration for telecom_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from main.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("blog/", blog, name="blog"),
    path("blog-details/<int:blog_id>/", blog_details),
    path("news/<int:news_id>/", news_detail),
    path("register/", register_view, name="register_view"),
    path("login/", login_view, name="login_view"),
    path("contact/", contact, name="contact"),
    path("logout/", logout_view, name="logout_view"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("telecomwifi/", telecomwifi, name="telecomwifi"),
    path("internetcafe/", internet_cafe, name="internet_cafe"),
    path("tariffs/", tariffs, name="tariffs"),
    path("hosting/", hosting, name="hosting"),
    path("hosting_virtual/", hosting_virtual, name="hosting_virtual"),
    path("hosting_physical/", hosting_physical, name="hosting_physical"),
    path("telewideniye/", telewideniye, name="telewideniye"),
    path("telephone/", telephone, name="telephone"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
