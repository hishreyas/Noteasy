from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from .models import Notice, User,Course
from .forms import NewNoticeForm,ChangeNoticeForm
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class NoticeListView(ListView):
	model = Notice
	context_object_name = 'notices'
	template_name = 'notices/home.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		return super().get_context_data(**kwargs)

	def get_queryset(self):
		queryset = Notice.objects.order_by('-created_at')
		return queryset



class UserNoticeListView(LoginRequiredMixin, ListView):
	model = Notice
	context_object_name = 'notices'
	template_name = 'notices/notices_by_user.html'
	paginate_by = 10
	

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)		
		context_data['selected_user'] = self.kwargs['selected_user']
		return context_data

	def get_queryset(self):
		self.selected_user = get_object_or_404(User, username=self.kwargs['selected_user'])
		return Notice.objects.filter(created_by=self.selected_user).order_by('-created_at')


class TagView(LoginRequiredMixin, ListView):
	model = Notice
	context_object_name = 'notices'
	template_name = 'notices/tag.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)		
		context_data['tag'] = self.kwargs['tag']
		return context_data

	def get_queryset(self):
		return Notice.objects.filter(tags__icontains=self.kwargs['tag']+',').order_by('-created_at')


@login_required
def TagListView(request) :
	queryset = Notice.objects.filter(tags__isnull=False).values_list('tags', flat=True)
	tags = set(''.join(queryset).split(',')[:-1])
	return render(request, 'notices/tags.html', {'tags': tags})

@login_required
def NoticeView(request, notice_id) :
	notice = get_object_or_404(Notice, id = notice_id)
	return render(request, 'notices/notice_page.html', {'notice': notice})


@staff_member_required
def NewNoticePage(request):
	if request.method == 'POST':
		form = NewNoticeForm(request.POST)
		if form.is_valid():
			notice = form.save(commit=False)
			notice.created_by = request.user
			if(request.user.course not in  notice.tags ):
				notice.tags=notice.tags+request.user.course+','
			notice.save()
			return redirect('notices:notice_page', notice_id=notice.pk) 
	else:
		form = NewNoticeForm()
	return render(request, 'notices/new_notice.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class NoticeChangeView(UpdateView):
	form_class = ChangeNoticeForm
	template_name = 'notices/update_notice.html'

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)		
		context_data['notice_id'] = self.kwargs['notice_id']
		return context_data
		
	def get_success_url(self):
		return reverse_lazy('notices:notice_page',kwargs={'notice_id': self.kwargs['notice_id']})	
	
	def get_object(self):
		notice = get_object_or_404(Notice, id = self.kwargs['notice_id'])
		if(self.request.user.id==notice.created_by.id):
			return notice
		else:
			raise ValueError('No permission to perform task'	)

@method_decorator(login_required, name='dispatch')
class NoticeDeleteView(DeleteView):
	template_name = 'notices/delete_notice.html'

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)		
		context_data['notice_id'] = self.kwargs['notice_id']
		return context_data
		
	def get_success_url(self):
		return reverse_lazy('notices:home')	
	
	def get_object(self):
		notice = get_object_or_404(Notice, id = self.kwargs['notice_id'])
		if(self.request.user.id==notice.created_by.id):
			return notice
		else:
			raise ValueError('No permission to perform task'	)			
			
