from django.db import models


class Task(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)
