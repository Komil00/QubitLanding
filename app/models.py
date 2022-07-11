from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils.safestring import mark_safe


class Category(models.Model):
    title = models.CharField(max_length=35)
    icon = models.ImageField(upload_to='media')
    cover = models.ImageField(upload_to='media')
    description = models.CharField(max_length=100)

    def image_tag1(self):
        if self.icon != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.icon))

    def image_tag2(self):
        if self.cover != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.cover))

    def __str__(self):
        return self.title


class Project(models.Model):
    name = models.CharField(max_length=35)
    cover = models.ImageField(upload_to='media')
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    def image_tag(self):
        if self.cover != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.cover))

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=100)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.image))

    def __str__(self):
        return self.project.name


class Contact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    contact = models.CharField(max_length=3000)
    created = models.DateField()
    update = models.DateField()

    def __str__(self):
        return self.fullname


class ArticleCategory(models.Model):
    title = models.CharField(max_length=35)
    icon = models.ImageField(upload_to='media')

    def image_tag(self):
        if self.icon != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.icon))

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=35)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=35)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='media')
    context = models.TextField(max_length=5000)
    tags = models.ManyToManyField(Tag)
    likes = models.PositiveSmallIntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateField()
    update = models.DateField()

    def image_tag(self):
        if self.cover != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.cover))

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=35)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='media')
    description = models.CharField(max_length=100)
    price = models.FloatField()

    def image_tag(self):
        if self.cover != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.cover))

    def __str__(self):
        return self.title
