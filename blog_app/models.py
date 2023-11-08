from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField




# Create your models here.

#here is post model 
class Post(models.Model):
    title=models.CharField(max_length=200)
    title_tag=models.CharField(max_length=200, default="Anand Blogs")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categary=models.CharField(max_length=255, default="coding")
    body = RichTextField(blank=True, null= True)
   # body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User, related_name='blog_posts')
    header_image=models.ImageField(null=True , blank=True, upload_to='images/')

    def __str__(self):
     return f"{self.title} | {self.author}"
    
    def get_absolute_url(self):
       # return reverse("article-detail", args=(str(self.id),))
       return reverse('home')
    

class Category(models.Model):
   name = models.CharField(max_length=255)

   def __str__(self):
       return self.name
   
   def get_absolute_url(self):
       # return reverse("article-detail", args=(str(self.id),))
       return reverse('home')
   

class HomeContent(models.Model):
   blog_heading = models.CharField(max_length=255)
   blog_heading_body = models.TextField()


class Comment(models.Model):
   post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
   name = models.CharField(max_length=255)
   body = models.TextField()
   date_dated = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return '%s - %s' % (self.post.title, self.name)
   

    

