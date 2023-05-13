from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Forum(models.Model):
    # Forum fields and relationships
    title = models.CharField(max_length=100)
    forum_slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + "....."
    
    def save(self, *args, **kwargs):
        if not self.forum_slug:
            self.forum_slug = slugify(self.title)
        super(Forum, self).save(*args, **kwargs)


class Topic(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    # Topic fields and relationships
    ttitle = models.CharField(max_length=100)
    topic_slug = models.SlugField(unique=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    tbody = models.TextField()
    tdate = models.DateTimeField(auto_now_add=True)
    tauthor = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.ttitle
    
    def save(self, *args, **kwargs):
        if not self.topic_slug:
            self.topic_slug = slugify(self.ttitle)
        super(Topic, self).save(*args, **kwargs)

    def snippet(self):
        return self.tbody[:50] + "....."
    
    
class Comment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    cauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    cbody = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cbody