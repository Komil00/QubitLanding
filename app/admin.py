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
    list_display = ['name', 'cover', 'category']
    inlines = [
        ProjectInline,
    ]


admin.site.register(ProjectImage)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(ArticleCategory)
admin.site.register(Article)
admin.site.register(Service)
admin.site.register(Tag)
