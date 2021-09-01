from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Live
from .forms import LiveForm


def live_list(request):
    template_name = 'live/live_list.html'
    object_list = Live.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def live_detail(request, pk):
    template_name = 'live/live_detail.html'
    return render(request, template_name)


def live_add(request):
    template_name = 'live/live_form.html'
    return render(request, template_name)


class LiveCreate(CreateView):
    model = Live
    template_name = 'live/live_form.html'
    form_class = LiveForm
    success_url = reverse_lazy('live:live_list')


def live_json(request):
    lives = Live.objects.all()
    data = [live.to_dict_json() for live in lives]
    return JsonResponse({'data': data})
