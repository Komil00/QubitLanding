from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category, Project, ProjectImage, Contact, ArticleCategory, Article, Tag, Service
from .serializers import *


class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class ProjectView(viewsets.ViewSet):
    queryset = Project.objects.all()

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProjectImageView(viewsets.ViewSet):
    queryset = ProjectImage.objects.all()

    def list(self, request):
        queryset = ProjectImage.objects.all()
        serializer = ProjectListImageSerializer(queryset, many=True)
        return Response(serializer.data)


class ContactView(viewsets.ViewSet):
    queryset = Contact.objects.all()

    def list(self, request):
        queryset = Contact.objects.all()
        serializer = ContactListSerializer(queryset, many=True)
        return Response(serializer.data)


class ArticleCategoryView(viewsets.ViewSet):
    queryset = ArticleCategory.objects.all()

    def list(self, request):
        queryset = ArticleCategory.objects.all()
        serializer = ArticleListCategorySerializer(queryset, many=True)
        return Response(serializer.data)


class TagView(viewsets.ViewSet):
    queryset = Tag.objects.all()

    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)


class ArticleView(viewsets.ViewSet):
    queryset = Article.objects.all()

    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleListSerializer(queryset, many=True)
        return Response(serializer.data)


class ServiceView(viewsets.ViewSet):
    queryset = Service.objects.all()

    def list(self, request):
        queryset = Service.objects.all()
        serializer = ServiceListSerializer(queryset, many=True)
        return Response(serializer.data)


