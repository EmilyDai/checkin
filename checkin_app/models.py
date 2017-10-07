from django.db import models
from django.utils.functional import cached_property
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from checkin_app import constant


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=256, null=False, default='')
    description = models.TextField(max_length=256, default="", blank=True)
    image  = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def projects(self):
        return UserProject.objects.filter(user_id=self.pk)

    @cached_property
    def records(self):
        return Records.objects.filter(user_id=self.pk)

    @cached_property
    def comments(self):
        return Comment.objects.filter(comment_to=self.pk)


class Tag(models.Model):
    name = models.CharField(max_length=256, null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=256, null=False, default='')
    notice = models.CharField(max_length=512)
    tag = models.ForeignKey(Tag)
    duration = models.IntegerField(default=0, null=True)
    frequency = models.CharField(max_length=256, null=False, default='')
    remedy_pemission = models.BooleanField(default=False)
    diary_need = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def cached_tag(self):
        return Tag.objects.get(pk=self.tag_id)

class UserProject(models.Model):
    user_id = models.BigIntegerField(db_index=True)
    project = models.ForeignKey(Project)
    status = models.CharField(max_length=64,
                              choices=constant.STATUS_CHOICES,
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Record(models.Model):
    user_id = models.BigIntegerField(db_index=True)
    project = models.ForeignKey(Project)
    checkin_date = models.DateField()
    checkin_time = models.DateTimeField(default=timezone.now)
    num_checkin_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user_id", "checkin_date")
        ordering = ['-created_at']

    @cached_property
    def cached_project(self):
        return Project.objects.get(pk=self.project_id)

class Diary(models.Model):
    user_id = models.BigIntegerField(db_index=True)
    record = models.ForeignKey(Record)
    name = models.CharField(max_length=256, null=False, default='')
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def cached_record(self):
        return Record.objects.get(pk=self.record_id)

class Comment(models.Model):
    user_id = models.BigIntegerField(db_index=True)
    comment_to = models.BigIntegerField(db_index=True, null=True)
    diary = models.ForeignKey(Diary)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def cached_diary(self):
        return Diary.objects.get(pk=self.diary_id)
