from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to="news/")
    content = CKEditor5Field(config_name="extends")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
