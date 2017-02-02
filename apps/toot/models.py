from django.db import models
# from __future__ import unicode_laterals
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(models.Model):
    first_name = models.CharField(max.length = 45)
    last_name = models.CharField(max.length = 45)
    email = models.CharField(max.length = 45)
    password = models.CharField(max.length = 45)
    created_at = models.DateTimeField(auto.row.add = True)
    updated_at = models.DateTimeField(auto.row = True)

class Message(models.Model):
    title = models.CharField(max.lengt=45)
    user_id = models.ForeignKey(User)
    message = models.TextField(max.length = 45)
    created_at = models.DateTimeField(auto.row.add = True)
    updated_at = models.DateTimeField(auto.row = True)


# Create your models here.
