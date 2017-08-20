from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import date
from checkin_app.serializers import (UserSerializer, TagSerializer,
    RuleSerializer, ProjectSerializer, RecordSerializer, DiarySerializer,
    CommentSerializer, CustomUserSerializers, UserProjectSerializer)
from checkin_app.models import (Tag, Rule, CustomUser, Project, Record, Diary,
    Comment, UserProject)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customuser = self.get_object(pk)
        serializer = CustomUserSerializers(customuser)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customuser = self.get_object(pk)
        serializer = CustomUserSerializers(customuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customuser = self.get_object(pk)
        customuser.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TagList(APIView):
    def get(self, request):
        tags = Tag.objects.all()
        s_tags = TagSerializer(tags, many=True)
        return Response(s_tags.data)

    def post(self, request):
        data = request.data
        tag = Tag.objects.create(**data)
        return Response(TagSerializer(tag).data,
            status=status.HTTP_201_CREATED)

class TagDetail(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def put(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        for k, v in request.data.items():
            setattr(tag, k, v)
        tag.save()
        return Response(TagSerializer(tag).data)

class RuleList(APIView):
    def get(self, request):
        rules = Rule.objects.all()
        s_rules = RuleSerializer(rules, many=True)
        return Response(s_rules.data)

    def post(self, request):
        data = request.data
        tag = Rule.objects.create(**data)
        return Response(RuleSerializer(tag).data,
            status=status.HTTP_201_CREATED)

class RuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def put(self, request, pk):
        rule = Rule.objects.get(pk=pk)
        for k, v in request.data.items():
            setattr(tag, k, v)
        rule.save()
        return Response(RuleSerializer(rule).data)

class ProjectList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        s_projects = ProjectSerializer(projects, many=True)
        return Response(s_projects.data)

    def post(self, request):
        data = request.data
        project = Project.objects.create(**data)
        return Response(ProjectSerializer(project).data,
            status=status.HTTP_201_CREATED)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class UserProjectList(APIView):
    def get(self, request):
        projects = UserProject.objects.filter(user_id=request.user.id)
        return Response(UserProjectSerializer(projects, many=True).data)

    def post(self, request):
        data = request.data
        project_id = data['project_id']
        u_project = UserProject.objects.create(project_id=project_id,
            user_id=request.user.id)
        return Response(UserProjectSerializer(u_project).data,
            status=status.HTTP_201_CREATED)

class UserProjectDetail(generics.DestroyAPIView):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class RecordList(APIView):
    def get(self, request):
        records = Record.objects.filter(user_id=request.user.id)
        s_records = RecordSerializer(records, many=True)
        return Response(s_records.data)

    def post(self, request):
        data = request.data
        data['checkin_date'] = date.today()
        data['user_id'] = request.user.id
        try:
            record = Record.objects.get(user_id=request.user.id,
                project_id=data['project_id'],
                checkin_date=date.today())
            return Response(RecordSerializer(record).data)
        except Record.DoesNotExist:
            count = Record.objects.filter(user_id=request.user.id,
                project_id=data['project_id']).count()
            data['num_checkin_days'] = count + 1
            record = Record.objects.create(**data)
            return Response(RecordSerializer(record).data,
                status=status.HTTP_201_CREATED)


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def put(self, request, pk, format=None):
        try:
            record = Record.objects.get(pk=pk, user_id=request.user.id)
        except Record.DoesNotExist:
            return Http404
        for k, v in request.data.items():
            setattr(record, k, v)
        record.save()
        return Response(RecordSerializer(record).data)

class DiaryList(APIView):
    def get(self, request):
        diaries = Diary.objects.filter(user_id=request.user.id)
        s_diaries = DiarySerializer(diaries, many=True)
        return Response(s_diaries.data)

    def post(self, request):
        data = request.data
        data['user_id'] = request.user.id
        diary = Diary.objects.create(**data)
        return Response(DiarySerializer(diary).data,
            status=status.HTTP_201_CREATED)

class DiaryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer

    def put(self, request, pk, format=None):
        try:
            diary = Diary.objects.get(pk=pk, user_id=request.user.id)
        except Diary.DoesNotExist:
            return Http404
        for k, v in request.data.items():
            setattr(diary, k, v)
        diary.save()
        return Response(RecordSerializer(diary).data)

class CommentList(APIView):
    def get(self, request):
        data = request.query_params
        print('aaa')
        print(data)
        comments = Comment.objects.filter(diary_id=data['diary_id'])
        s_comments = CommentSerializer(comments, many=True)
        return Response(s_comments.data)

    def post(self, request):
        data = request.data
        data['user_id'] = request.user.id
        comment = Comment.objects.create(**data)
        return Response(CommentSerializer(comment).data,
            status=status.HTTP_201_CREATED)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, pk, format=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return Http404
        for k, v in request.data.items():
            setattr(comment, k, v)
        comment.save()
        return Response(CommentSerializer(comment).data)
