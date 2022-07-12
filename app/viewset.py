from rest_framework import viewsets, permissions
from .models import Category, Project, ProjectImage, Contact, ArticleCategory, Article, Tag, Service
from .serializers import CategorySerializer, ProjectListSerializer, ProjectPostSerializer, ProjectListImageSerializer, \
    ProjectPostImageSerializer, ContactListSerializer, ContactPostSerializer, ArticleListCategorySerializer, \
    ArticlePostCategorySerializer, TagSerializer, ArticleListSerializer, ArticlePostSerializer, ServiceListSerializer, \
    ServicePostSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        if self.action == "retrieve":
            return ProjectListSerializer
        else:
            return ProjectPostSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ProjectImageView(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListImageSerializer
        if self.action == "retrieve":
            return ProjectListImageSerializer
        else:
            return ProjectPostImageSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ContactListSerializer
        if self.action == "retrieve":
            return ContactListSerializer
        else:
            return ContactPostSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ArticleCategoryView(viewsets.ModelViewSet):
    queryset = ArticleCategory.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleListCategorySerializer
        if self.action == "retrieve":
            return ArticleListCategorySerializer
        else:
            return ArticlePostCategorySerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleListSerializer
        if self.action == "retrieve":
            return ArticleListSerializer
        else:
            return ArticlePostSerializer

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceListSerializer
        if self.action == "retrieve":
            return ServiceListSerializer
        else:
            return ServicePostSerializer
