from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)

    class Meta:
        verbose_name_plural = 'Searches'


class TodoList(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now())

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return "{} - {}".format(self.user, self.title)