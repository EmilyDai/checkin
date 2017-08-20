from django.db import models
from django.utils.functional import cached_property
from django.utils import timezone
from django.contrib.auth.models import User
from checkin_app import constant


class CustomUser(User):
    nickname = models.CharField(max_length=256, null=False, default='')
    description = models.TextField(max_length=256, default="", blank=True)
    image  = models.CharField(max_length=256, null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=256, null=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Rule(models.Model):
    duration = models.IntegerField(default=0)
    frequency = models.CharField(max_length=256, null=False, default='')
    remedy_pemission = models.BooleanField(default=False)
    diary_need = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=256, null=False, default='')
    notice = models.CharField(max_length=512)
    tag_id = models.PositiveIntegerField()
    rule_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @cached_property
    def cached_tag(self):
        return cache.get_model(Tag, pk=self.tag_id)

    @cached_property
    def cached_rule(self):
        return cache.get_model(Rule, pk=self.rule_id)

class UserProject(models.Model):
    user_id = models.BigIntegerField(db_index=True)
    project_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Record(models.Model):
    user_id = models.BigIntegerField(db_index=True)
    project_id = models.PositiveIntegerField(db_index=True)
    checkin_date = models.DateField()
    checkin_time = models.DateTimeField(default=timezone.now)
    num_checkin_days = models.IntegerField(default=0, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user_id", "checkin_date")
        ordering = ['-created_at']

    @property
    def cached_user(self):
        return cache.get_model(User, pk=self.user_id)

class Diary(models.Model):
    user_id = models.BigIntegerField(db_index=True)
    record_id = models.PositiveIntegerField()
    name = models.CharField(max_length=256, null=False, default='')
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cached_record(self):
        return cache.get_model(Record, pk=self.record_id)

class Comment(models.Model):
    user_id = models.BigIntegerField()
    diary_id = models.PositiveIntegerField()
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cached_diary(self):
        return cache.get_model(Diary, pk=self.diary_id)
