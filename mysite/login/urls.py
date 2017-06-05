from django.conf.urls import url

from . import views

from .models import User

app_name = 'login'

urlpatterns = [
    url(r'^$', views.login, name='login_home'),
    url(r'^register$', views.register, name='register'),
    url(r'^loginout$', views.loginout, name='loginout'),
    url(r'^index$', views.LoginIndex.as_view(), name='loginindex'),
]
