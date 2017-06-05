# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.views import generic
from .models import BasicInformation
from myself.settings import LOGIN_URL

class IndexView(generic.ListView):
    model = BasicInformation
    template_name = "resume/index.html"
    context_object_name = "basic_information_list"

from django.contrib.auth.decorators import login_required


def index(request):
    if 'user' in request.session:
        return render(request, 'resume/index.html',
            context={'basic_information_list': BasicInformation.objects.all(),
                'username': request.session['user']}
        )
    else:
        return HttpResponseRedirect(LOGIN_URL)


class AwardView(generic.ListView):
    model = BasicInformation
    context_object_name = "basic_information_list"


def award(request):
    return render(request, 'resume/award.html',
        context={'basic_information_list': BasicInformation.objects.all()}
    )


class IndexTemplateView(generic.TemplateView):
    template_name = "resume/index-template-view.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['basic_information_list'] = BasicInformation.objects.all()
        return context
