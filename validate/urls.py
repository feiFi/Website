from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^acc_register/',views.acc_register,name='acc_register'),
    url(r'^index/',views.index,name='index'),
    url(r'^login/',views.login,name='login'),
    url(r'^acc_login/',views.acc_login,name='acc_login'),

]
