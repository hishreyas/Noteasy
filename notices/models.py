from django.db import models
from accounts.models import  User
from django.utils.html import mark_safe
from markdown import markdown


class Notice(models.Model):
	title = models.CharField(max_length=100)
	message = models.TextField(max_length=2000)
	created_at = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=100, null=True)
	created_by = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.title

	def get_message_as_markdown(self):
		return mark_safe(markdown(self.message, safe_mode='escape', extensions=['tables','fenced_code']))

	def get_prefix_name(self):
		if(self.created_by.first_name!=None and self.created_by.last_name!=None):
			return self.created_by.first_name[0] + self.created_by.last_name[0]

		if(self.created_by.first_name!=None):
			return self.created_by.first_name[0]

		if(self.created_by.last_name!=None):
		   return self.created_by.last_name[0]
		   
		return self.created_by.username[0]
		
		

	       

	def get_tags_as_list(self):
		return self.tags.split(",")[:-1]