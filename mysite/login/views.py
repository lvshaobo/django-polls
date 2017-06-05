from django.shortcuts import render

# Create your views here.

from django.views import generic
from .models import User

from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())


def register(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact=username)
            print(user)
            if user:
                return HttpResponse(username + ' already exists')
            else:
                user = User()
                user.username, user.password = username, password
                user.save()
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/register/')
    else:
        uf = UserForm()
    return render(request, 'login/register.html', {'uf': uf})

def login(request):
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact=username,
                password__exact = password)
            if user:
                request.session['user'] = username
                return HttpResponseRedirect('/resume/')
                """
                return render(
                    request, 'login/success.html', 
                    {'user_list': User.objects.all()})
                """
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render(request, 'login/login.html', {'uf': uf})


def loginout(request):
    if 'user' in request.session:
        print('user: %s' %request.session['user'])
        del request.session['user']
    else:
        print('loginout')
    return HttpResponseRedirect('/login/')

class LoginIndex(generic.TemplateView):
    template_name = "login/index.html"

    def get_context_data(self, **kwargs):
        context = super(LoginIndex, self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context
    
