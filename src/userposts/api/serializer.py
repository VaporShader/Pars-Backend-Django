from rest_framework import serializers

from userposts.models import UserPosts


class UserPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosts
        fields = ('id', 'Avatar', 'Name', 'Date', 'Title', 'Media',
                  'Text', 'Likes', 'Dislikes')
