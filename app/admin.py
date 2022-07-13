from django.contrib import admin
from .models import *


class ProjectInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    def cover_image(self, obj):
        return mark_safe('<img src="{url}" width="60" height="60" />'.format(
            url=obj.cover.url,
            width=obj.cover.width,
            height=obj.cover.height,
        )
        )

    readonly_fields = ['cover_image']
    search_fields = ('name',)
    list_filter = ('category',)
    fields = ['name', 'cover', 'cover_image', 'description', 'category']
    list_display = ['name', 'category', 'image_tag']
    inlines = [
        ProjectInline,
    ]


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'image_tag']
    fields = ['title', 'icon', 'icon_image']

    def icon_image(self, obj):
        return mark_safe('<img src="{url}" width="60" height="60" />'.format(
            url=obj.icon.url,
            width=obj.icon.width,
            height=obj.icon.height,
        )
        )

    readonly_fields = ['icon_image']


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    search_fields = ('project',)
    list_display = ['project', 'image_tag', 'description']
    fields = ['project', 'image', 'image_image', 'description']

    def image_image(self, obj):
        return mark_safe('<img src="{url}" width="60" height="60" />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )

    readonly_fields = ['image_image']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'category', 'author', 'image_tag']
    fields = ['title', 'category', 'author', 'cover', 'cover_image', 'context', 'tags', 'likes', 'created', 'update']

    def cover_image(self, obj):
        return mark_safe('<img src="{url}" width="60" height="60" />'.format(
            url=obj.cover.url,
            width=obj.cover.width,
            height=obj.cover.height,
        )
        )

    readonly_fields = ['cover_image']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'icon_image', 'cover_image']
    fields = ['title', 'icon', 'icon_image', 'cover', 'cover_image']

    def icon_image(self, obj):
        return mark_safe(f'<img src="{obj.icon.url}" width="120" height="120" />')

    def cover_image(self, obj):
        return mark_safe(f'<img src="{obj.cover.url}" width="120" height="120" />')

    readonly_fields = ['icon_image', 'cover_image']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('fullname',)
    list_display = ['fullname', 'email', 'category', 'contact']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'category', 'price', 'image_tag']
    fields = ['title', 'category', 'price', 'cover', 'cover_image']

    def cover_image(self, obj):
        return mark_safe('<img src="{url}" width="60" height="60" />'.format(
            url=obj.cover.url,
            width=obj.cover.width,
            height=obj.cover.height,
        )
        )

    readonly_fields = ['cover_image']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ['title', 'id']

