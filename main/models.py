from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(null=True,blank=True,upload_to="images/")
    intro = models.CharField(max_length=2555)
    snippets_content = RichTextField(max_length=12000, null=True, blank=True)
    body = models.TextField()
    date_upload = models.DateTimeField("date published",default=datetime.now())


    class Meta:
        ordering = ['-date_upload']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    useremail = models.EmailField()
    usercomment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['comment_date']      

