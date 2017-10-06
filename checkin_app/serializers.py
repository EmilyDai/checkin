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
    class Meta:
        model = Project
        fields = ('id', 'name', 'notice', 'tag_id', 'created_at',
            'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class UserProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProject
        fields = ('id', 'project_id', 'user_id', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('id', 'user_id', 'project_id', 'checkin_date', 'checkin_time',
                  'num_checkin_days', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id', 'user_id', 'record_id', 'name', 'content', 'created_at',
            'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user_id', 'diary_id', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
