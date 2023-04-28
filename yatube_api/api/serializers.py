from rest_framework import serializers

from posts.models import Group, Post, Comment


class GroupSerializer(serializers.ModelSerializer):
    """
    GroupSerializer class related to Groups.

    This will refer to class Group in models file
    and output information as it shown below in fields.
    """
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """
    PostSerializer class related to Posts.

    This will refer to class Post in models file
    and output information as it shown below in fields.
    """
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """
    CommentSerializer class related to Comments.

    This will refer to class Comment in models file
    and output information as it shown below in fields.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ['post']
