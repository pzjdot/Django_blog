from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.shortcuts import render, redirect

from blogs.models import Blog, Category


def posts_by_category(request, category_id):
    # 获取 id 为 category id 的帖子
    posts = Blog.objects.filter(status='Published', category_id=category_id)
    # 当类别不存在的情况下
    try:
        category = Category.objects.get(pk=category_id)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        # 如果没有该类别，返回到用户主页
        return redirect('home')

    # 如果希望显示 404 错误页面使用 404
    # category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)
