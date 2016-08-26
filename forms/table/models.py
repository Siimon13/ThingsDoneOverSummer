from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

class Join(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class JoinForm(ModelForm):
    class Meta:
        model = Join
        fields = ['title','address']
