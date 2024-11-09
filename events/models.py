from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    description = models.TextField(verbose_name="Description")
    date = models.DateTimeField(verbose_name="Date")
    location = models.CharField(max_length=255, verbose_name="Location")
    limit = models.PositiveIntegerField(verbose_name="Limit")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Category")
    tags = models.ManyToManyField('Tag', blank=True, related_name="events", verbose_name="Tags")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    
    def get_responses_count(self):
        return Response.objects.filter(event=self).count()

    def get_absolute_url(self):
        return f'/events/{self.id}'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Event")

    def __str__(self):
        return f"{self.user.username} responsed on {self.event.title}"
    

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Event")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created ad")

    def get_absolute_url(self):
        return f'/events/{self.event.id}'

    def __str__(self):
        return f"Comment from {self.author} on {self.event}"
