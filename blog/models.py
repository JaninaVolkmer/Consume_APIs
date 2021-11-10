from django.db import models

# Create your models here.
"""
Create 3 separate database tables which need to be related
to one another:
:Category
:Post:
- auto_add_now: assigns current date/time to field when instance of
  class is created
- auto_add: assigns current date/time to field when instance of class is saved
- ManyToManyField: create relationship Post + Category
:Comment:
- ForeignKey: many-to-one relationship (many comments to one post)
"""


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
