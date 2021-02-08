from rest_framework.viewsets import ModelViewSet
from userposts.models import UserPosts
from .serializer import UserPostsSerializer


class UserPostsViewSet(ModelViewSet):
    queryset = UserPosts.objects.all()
    serializer_class = UserPostsSerializer
