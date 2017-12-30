from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
# Create your models here.

class RantQuerySet(models.QuerySet):
    def rant(self, dtitle):
        return self.filter(title=dtitle)
    def top_rants():
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
    author = models.ForeignKey(User , null=True, blank=True)
    category = models.CharField(max_length=1, choices=CATIGORIES, default='Everyday Living')
    objects = RantQuerySet.as_manager()
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=80, default="anonymous")
    rant = models.ForeignKey(Rant, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created']
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.rant)
