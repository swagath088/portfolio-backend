from django.db import models
from django.contrib.auth.models import User

# ------------------------------
# Project Model
# ------------------------------

from cloudinary.models import CloudinaryField

# ------------------------------
# Project Model
# ------------------------------
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.TextField()
    github_link = models.URLField()
    live_link = models.URLField(blank=True, null=True)
    image = CloudinaryField('image', blank=True, null=True)  # Direct Cloudinary upload

    def __str__(self):
        return self.title

# ------------------------------
# Blog Model
# ------------------------------
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)  # Direct Cloudinary upload
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ------------------------------
# Contact Model
# ------------------------------
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

# ------------------------------
# Skill Model
# ------------------------------
class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)  # 0-100 scale

    def __str__(self):
        return self.name

# ------------------------------
# Message Model
# ------------------------------
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
