from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post

def post_list(request):
    q = request.GET.get('q')

    posts = Post.objects.all()

    if q:
        posts = posts.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/list.html', {
        'page_obj': page_obj,
    })