from .viewset import (CategoryView,
                      ProjectView,
                      ProjectImageView,
                      ContactView,
                      ArticleCategoryView,
                      TagView,
                      ArticleView, ServiceView)

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'project', ProjectView)
router.register(r'projectimage', ProjectImageView)
router.register(r'contact', ContactView)
router.register(r'articlecategory', ArticleCategoryView)
router.register(r'tag', TagView)
router.register(r'article', ArticleView)
router.register(r'service', ServiceView)
urlpatterns = router.urls
