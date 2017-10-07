from rest_framework import serializers
from django.contrib.auth.models import User
from checkin_app.models import Tag, Project, Record, \
                                Diary, Comment, CustomUser, UserProject


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        read_only_fields = ('id', )

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'nickname', 'description',
            'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('id', 'name', 'created_at', 'updated_at')

class ProjectSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    class Meta:
        model = Project
        fields = "__all__"

class UserProjectSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = UserProject
        fields = "__all__"

class RecordSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    class Meta:
        model = Record
        fields = "__all__"

class DiarySerializer(serializers.ModelSerializer):
    record = RecordSerializer()
    class Meta:
        model = Diary
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    diary = DiarySerializer
    class Meta:
        model = Comment
        fields = "__all__"
