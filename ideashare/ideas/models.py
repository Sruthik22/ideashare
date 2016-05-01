from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User)
    votes = models.IntegerField(default = 0)
    def __str__(self):
    	return self.content

class Comment(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	author = models.ForeignKey(User)
	Post = models.ForeignKey(Post)
	def __str__(self):
		return self.content
		