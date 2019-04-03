from django.conf.urls import url
from QuNaApp import views

app_name = 'app'
urlpatterns = [
    # url(r'^/', views.index),
    url(r'^get_data/$', views.get_data, name='get_data'),
    url(r'^get_LvyouNote/(\d+?)/$', views.get_LvyouNote, name='get_LvyouNote'),
    url(r'^do_predict/', views.do_predict, name='do_predict'),
]
