from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if User gets deleted, posts from the user also get deleted; many to one relationship

    def __str__(self): #provides the name of the model; eg: if you have a Post object with the title "My First Post", calling str(post) or print(post) will return "My First Post".
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})