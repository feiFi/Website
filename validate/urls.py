from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^acc_register/',views.acc_register,name='acc_register'),

]
