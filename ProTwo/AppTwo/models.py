from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name


class Chapter(models.Model):
    chaptername = models.CharField(max_length=264, unique=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.chaptername


class Users(models.Model):
    Firstname = models.CharField(max_length=264)
    Lastname = models.CharField(max_length=264)
    Email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.Email
