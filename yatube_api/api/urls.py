from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()


router.register('groups', GroupViewSet, basename='groups')
router.register('posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>\\d+)/comments',
                CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
]
