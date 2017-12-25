from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RantQuerySet(models.QuerySet):
    def rant(self, dtitle):
        return self.objects.filter(title=dtitle)
    def top_rants():
        pass

class Rant(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    time_created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User , null=True, blank=True)
    objects = RantQuerySet()
