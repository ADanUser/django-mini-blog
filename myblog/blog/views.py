from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import BlogPost, Likes
from .form import CommentForm

class BlogPostView(View):
    '''вывод записей'''
    def get(self, request):
        blog_posts = BlogPost.objects.all()
        return render(request, 'blog/blog_post.html', {'post_list': blog_posts})

class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = BlogPost.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'post': post})

class AddComment(View):
    '''добавление комментария к записи'''
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = pk
            comment.save()
        return redirect(f'/{pk}/')
    
def get_client_ip(request):
    '''получение IP адреса клиента'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    '''добавление лайка к записи'''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id=pk)
            return redirect(f'/{pk}/')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}/')
        
class DelLike(View):
    '''удаление лайка у записи'''
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client, post_id=pk)
            like.delete()
            return redirect(f'/{pk}/')
        except:
            return redirect(f'/{pk}/')