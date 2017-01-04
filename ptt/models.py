from django.db import models

class Softjob(models.Model):
    author = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=100,null=True)
    content = models.TextField(null=True)
    page_index = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=100,null=True)
    comments = models.TextField(null=True)

    def __str__(self):
    	return self.title

