from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="news/")
    content = CKEditor5Field(config_name="extends")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    name = models.CharField(max_length=500)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    content = CKEditor5Field(config_name="extends")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.TextField()
    sent_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
