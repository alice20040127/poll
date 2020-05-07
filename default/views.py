from django.shortcuts import render
from .models import poll
from django.views.generic import ListView, DetailView

# Create your views here.
class PollList(ListView):
    model = Poll
class PollList(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['option_list'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return data