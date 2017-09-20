from django.db import models
from validate.models import User

STATUS = {
    0: u'正常',
    1: u'草稿',
    2: u'删除',
}


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


class Blog(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=50)

    contents = models.TextField()
    picture = models.ImageField(
        upload_to='/static/images', null=True, blank=True)
    author = models.ForeignKey(User)

    tages = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    is_top = models.BooleanField(default=False, verbose_name=u'置顶')
    status = models.IntegerField(default=0, choices=STATUS.items(),
                                 verbose_name='状态')

    view_count = models.IntegerField(editable=False, default=0)
    thumbs_up = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(User)
    publish_Time = models.DateTimeField(auto_now_add=True, auto_now=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    content = models.TextField()
    root_id = models.IntegerField(default=0)  # 评论的最上层评论，若该评论处于最上层，则为0，
    parent_id = models.IntegerField(default=0)  # 评论的父评论，若无父评论，则为0

    def __str__(self):
        return self.content
