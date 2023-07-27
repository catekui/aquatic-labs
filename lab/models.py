from django.db import models
from django.utils import timezone

# Create your models here.
class Publications(models.Model):
    author = models. CharField(max_length=150)
    title = models.CharField(max_length=100)


# class Posts(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
class Blog(models.Model):
    author = models. CharField(max_length=150)
    blog_title = models.CharField(max_length=400, verbose_name="Put aTitle")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name='What is on your mind')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name="blog image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title