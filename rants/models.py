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
    body = models.TextField(max_length=400)
    time_created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User , null=True, blank=True)
    category = models.CharField(max_length=1, choices=CATIGORIES, default='Everyday Living')
    objects = RantQuerySet.as_manager()
    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    rant = models.ForeignKey(Rant)
