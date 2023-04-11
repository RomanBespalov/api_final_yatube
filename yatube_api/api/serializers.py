from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.fields import CurrentUserDefault

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username', default=CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username', read_only=False, queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписались на этого пользователя'
            ),
        )

    def validate_following(self, value):
        """Нельзя подписываться на себя"""
        if Follow.objects.filter(user=value).exists():
            raise serializers.ValidationError(
                'Вы не можете подписаться на самого себя'
            )
        return value


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group
