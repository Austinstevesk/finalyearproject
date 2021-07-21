from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from .models import Consumer
from django.contrib.auth.models import User
from django.urls import reverse


#Create your views here.

def mygaslevels(request):
	user = User.objects.get(username = request.user.username)
	#user = get_object_or_404(User, User.username)
	context = {'consumer_details': Consumer.objects.all()}#filter(username=user)}
	return render(request, 'Consumers/mygaslevels.html', context)


# class ConsumerListView(ListView):
# 	model = Consumer
# 	template_name = 'Consumers/mygaslevels.html' # <app>/<model>_<viewtype>.html
# 	#context_object_name = 'posts' #Getting the data in the home view from the db
# 	ordering = ['-date'] #order gasleves from newest to oldest

# 	def get_queryset(self):
# 		user = get_object_or_404(User, username=self.kwargs.get('username'))
# 		return Consumer.objects.filter(username=user).order_by('-date')


class ConsumerView(TemplateView):
    template_name = 'Consumers/mygaslevels.html'

    def get(self, request, *args, **kwargs):
        demos = Consumer.objects.filter(username=User.objects.get (username=request.user)).order_by('-date')
        context = {
            'demos': demos,
        }
        return render(request, self.template_name, context)
