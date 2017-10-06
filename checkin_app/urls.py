from django.conf.urls import url
from checkin_app import views

urlpatterns = [
	url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
	url(r'^customusers/(?P<pk>[0-9]+)/$', views.CustomUserDetail.as_view()),
	url(r'^tags/$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
	url(r'^projects/$', views.ProjectList.as_view()),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view()),
	url(r'^userprojects/$', views.UserProjectList.as_view()),
	url(r'^userprojects/(?P<pk>[0-9]+)/$', views.UserProjectDetail.as_view()),
	url(r'^records/$', views.RecordList.as_view()),
    url(r'^records/(?P<pk>[0-9]+)/$', views.RecordDetail.as_view()),
	url(r'^diaries/$', views.DiaryList.as_view()),
    url(r'^diaries/(?P<pk>[0-9]+)/$', views.DiaryDetail.as_view()),
	url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
]
