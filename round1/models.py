from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Submission(models.Model):
    owner=models.ForeignKey(User)
    s_key = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    text_description = models.TextField(max_length=1024)
    date_created = models.DateTimeField(editable=False, auto_now_add=True)
class Author(models.Model):
    a_key=models.AutoField(primary_key=True)
    piece=models.ForeignKey(Submission)
    comp_id=models.CharField(max_length=16)
class mp3_file(models.Model):
    m_key=models.AutoField(primary_key=True)
    submitted=models.ForeignKey(Submission)
class lyric_file(models.Model):
    l_key=models.AutoField(primary_key=True)
    submitted=models.ForeignKey(Submission)