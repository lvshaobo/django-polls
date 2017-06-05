from django.conf.urls import url

from . import views

from .models import BasicInformation

app_name = 'resume'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.IndexView.as_view(), name='index_home'),
    url(r'^award$', views.AwardView.as_view(template_name="resume/award.html"), name='award'),
    url(r'^index-template-view$', views.IndexTemplateView.as_view(), name='index-template-view'),
]
