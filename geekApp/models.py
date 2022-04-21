from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100,null=True )

    email = models.EmailField(max_length=100,null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL )
    age = models.IntegerField()
    Des_yrself = models.TextField(null=True)
    Location = models.CharField(max_length=200, null=True)
    # pass

    def __str__(self):
        return self.Location


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    body = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    you = models.CharField(max_length=100)


    def __str__(self):
        # return self.title
        return f'{self.title} -- {self.author} -- {self.tag} '
