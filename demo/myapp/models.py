# models.py

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class SvgImage(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    editors = models.ManyToManyField(User, related_name='editable_images')
    description = models.TextField(blank=True, null=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='images')

    def __str__(self):
        return self.name

class Rectangle(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(SvgImage, related_name='rectangles', on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return f'Rectangle ({self.x}, {self.y}, {self.width}, {self.height}, {self.color})'
