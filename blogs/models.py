from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 修改复数
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


STATUS_CHOICE = (
    ('Draft', "Draft"),
    ('Published', "Published")
)


class Blog(models.Model):
    # 标题
    title = models.CharField(max_length=50)
    # slug
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    # 类别
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 特色图片
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    # 简介
    short_description = models.TextField(max_length=500)
    # 博客主体
    blog_body = models.TextField(max_length=500)
    # 状态 草稿或者已发布
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Draft')
    # 是否为精选文章
    is_featured = models.BooleanField(default=False)
    # 创建时间
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title





