from django.contrib import admin
from .models import *


class ProjectInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('category',)
    fields = ['name', 'cover', 'description', 'category']
    list_display = ['name', 'category', 'image_tag']
    inlines = [
        ProjectInline,
    ]


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'image_tag']


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    search_fields = ('project',)
    list_display = ['project', 'image_tag', 'description']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'category', 'author', 'image_tag']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'image_tag1', 'image_tag2']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('fullname',)
    list_display = ['fullname', 'email', 'category', 'contact']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'category', 'price', 'image_tag']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'id']
