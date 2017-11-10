import re

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Blog
from markdown import markdown


def blog_index(request):
    categories = Category.objects.all()
    return render(request,
                  'blog_index.html',
                  {'categories': categories})


def blog_page(request, temp):
    page = request.GET.get('page')

    if temp == "blog_main":
        blogs = Blog.objects.all()
        for blog in blogs:
            blog.contents = re.sub(
                r'[/#\[\]]*', "", blog.contents)  # re.sub(,"",a)
    else:
        category = Category.objects.filter(category_name=temp)
        blogs = Blog.objects.filter(category=category)
    paginator = Paginator(blogs, 1)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blogs = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blogs = paginator.page(paginator.num_pages)
    return render(request,
                  'includes/blog_page.html',
                  {'title': temp,
                   'blogs': blogs})


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.contents = markdown(blog.contents)
    return render(request,
                  'includes/blog_detail.html',
                  {'blog':blog})
