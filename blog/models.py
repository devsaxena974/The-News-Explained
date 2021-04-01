from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    short_description = RichTextField(blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default = 0)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    image_source = models.CharField(max_length=600, null=True, blank=True)
    

    class Meta:
        ordering = ['-created_on']
        get_latest_by = ['created_on']

    def __str__(self):
        return self.title

class Email(models.Model):
    text = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.text

class Extras(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    short_description = RichTextField(blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    image_source = models.CharField(max_length=600, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title