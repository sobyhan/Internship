from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url (r'^$', views.IndexView.as_view(), name = 'index'),
    url (r'^(?P<question_id>[0-9]+)/$', views.details, name='details'),
    url (r'^(?P<question_id>[0-9]+)/results/$', views.result, name='results'),
    url (r'^(?P<question_id>[0-9]+)/votes/$', views.vote, name='votes'),

]