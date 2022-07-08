from rest_framework import viewsets
from .models import Category, Project, ProjectImage, Contact, ArticleCategory, Article, Tag, Service
from .serializers import *


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        if self.action == "retrieve":
            return ProjectListSerializer
        else:
            return ProjectPostSerializer


class ProjectImageView(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListImageSerializer
        if self.action == "retrieve":
            return ProjectListImageSerializer
        else:
            return ProjectPostImageSerializer


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ContactListSerializer
        if self.action == "retrieve":
            return ContactListSerializer
        else:
            return ContactPostSerializer


class ArticleCategoryView(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleListCategorySerializer
        if self.action == "retrieve":
            return ArticleListCategorySerializer
        else:
            return ArticlePostCategorySerializer


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleListSerializer
        if self.action == "retrieve":
            return ArticleListSerializer
        else:
            return ArticlePostSerializer


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceListSerializer
        if self.action == "retrieve":
            return ServiceListSerializer
        else:
            return ServicePostSerializer
