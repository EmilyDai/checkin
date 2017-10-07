from django.contrib import admin
from checkin_app.models import CustomUser, Tag, Project

admin.site.register(CustomUser)
admin.site.register(Tag)
admin.site.register(Project)
