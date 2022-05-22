
from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
		path('',views.landingPage,name="landing"),
		path('home/', views.NoticeListView.as_view(), name='home'),
		path('notices/<int:notice_id>', views.NoticeView, name='notice_page'),
		path('notice/new', views.NewNoticePage, name='new_notice'),
		path('tag/<tag>', views.TagView.as_view(), name='tag'),
		path('tags', views.TagListView, name='tags'),
		path('u/<selected_user>', views.UserNoticeListView.as_view(), name='user_notices'),
		path('notice/update/<notice_id>', views.NoticeChangeView.as_view(), name='update_notice'),
		path('notice/delete/<notice_id>', views.NoticeDeleteView.as_view(), name='delete_notice')
		]