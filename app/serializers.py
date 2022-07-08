from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProjectListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ProjectPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ProjectListImageSerializer(serializers.ModelSerializer):
    project = ProjectListSerializer()

    class Meta:
        model = ProjectImage
        fields = '__all__'


class ProjectPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'


class ContactListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'


class ContactPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ArticleListCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializer(read_only=True)

    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticlePostCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleCategory
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    category = ArticleListCategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class ServiceListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Service
        fields = '__all__'


class ServicePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

