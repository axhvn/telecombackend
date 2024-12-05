from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("name", "publisher", "created_at", "updated_at")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "email", "sent_in")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
