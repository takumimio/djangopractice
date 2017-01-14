from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    POST_TYPE_CHOICES = (
        ('1', '一般文章'),
        ('2', '作品'),
    )
    post_type = models.CharField(max_length=1,choices=POST_TYPE_CHOICES,default='1')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.text

    def leave(self, user): 
        self.save()


class Subject(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

    def create(self, user): 
        self.save()
