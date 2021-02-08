from .views import UserPostsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserPostsViewSet, basename='userposts')
urlpatterns = router.urls
