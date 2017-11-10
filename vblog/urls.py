from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_index,name='blog_index'),
    url(r'blog_page/(\w+)/$',views.blog_page,name='blog_page'),
    url(r'blog_detail/(\d+)/$',views.blog_detail,name='blog_detail'),


]
