from django.shortcuts import render, get_object_or_404
from .models import *


def main(request):
    pass

def list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

def new(request):
    pass

def new(request):
    pass

def edit(request, post_id):
    pass

def delete(request, post_id):
    pass

def new_comment(request, post_id):
    comment = Comment()
    comment.post = get_object_or_404(Post, pk=post_id)
    comment.writer = request.user
    comment.phone_number = request.user.phone_number ##여기도 유저랑 통일해야 함
    comment.text = request.POST.get('text') ##주의 요망
    comment.save()
    return redirect('detail', post_id)

def del_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect('detail', post_id)