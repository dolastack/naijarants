from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.core.files.storage import FileSystemStorage
from django.urls import reverse, reverse_lazy
from django.utils import timezone
# Create your models here.


class RantQuerySet(models.QuerySet):
    def rant(self, dtitle):
        return self.filter(title=dtitle)
    def rant_of_type(self, dcategory):
        return self.filter(category=dcategory)
    def top_rants(self):
        pass

CATIGORIES = (
    ('E', 'Everyday Living'), ('P', 'Politics'),
    ('G','Religion'), ('R', 'Relationship'),
     ('S','Sex'), ('O', 'Other')
)

class Rant(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , null=True, blank=True , on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=CATIGORIES, default='Everyday Living')
    updated = models.DateTimeField(auto_now_add=True)
    files = models.FileField(upload_to='file-uploads/%Y/%m/%D/', blank=True )
    #image = models.ImageField( blank=True )
    objects = RantQuerySet.as_manager()
    class Meta:
        ordering = ['-time_created']
    def get_absolute_url(self):
        return reverse('rant_detail', args=[self.id, self.title])
    
    def get_social_url(self):
        url = "http://naijarants.com" + self.get_absolute_url()
        return url
    def get_tweet_text(self):
        #url = self.get_social_url().replace(" ", '%20')
        text = str(self.title).replace(" ", '%20')
        #tweet_text = '{0}%0A"{1}"'.format(text, url)
        return text
    def get_encoded_url(self):
        url = self.get_social_url().replace(" ", '%20')
        return url
    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=80, default="anonymous")
    rant = models.ForeignKey(Rant, related_name='comments', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created']
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.rant)
