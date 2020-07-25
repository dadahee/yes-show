from django.shortcuts import render,redirect,get_object_or_404
from .models import *

def main(request):
    return render(request,'content/main.html')

def list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})

def new(request):
    return render(request, 'new.html')

def postcreate(request):
    print(request.method)
    if(request.method == 'POST'):
      #<form action="{% url 'postcreate' %}" method="post">
      #hello/templates/postnew.html 파일 메서드 확인
        post = Post()
        post.writer = request.user
        post.title = request.POST['title']
        post.status = request.POST['status']
        post.reserve_price = request.POST['reserve_price']
        post.food_price = request.POST['food_price']
        post.people = request.POST['people']
        post.text = request.POST['text']
        post.save()
    return redirect('list')


def postupdate(request,post_id):
    editpost=get_object_or_404(Post,pk=post_id)
    editpost.title=request.POST['title']
    editpost.status = request.POST['status']
    editpost.reserve_price = request.POST['reserve_price']
    editpost.food_price = request.POST['food_price']
    editpost.people = request.POST['people']
    editpost.text = request.POST['text']
    editpost.save()
    return redirect('/content/'+str(post_id))


def detail(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request,'detail.html',{'comments':comments, 'post':post})

def edit(request,post_id):
    post=get_object_or_404(Post,pk=post_id)
    return render(request,'edit.html',{'post':post})

def delete(request,post_id):
    deletepost=get_object_or_404(Post,pk=post_id)
    deletepost.delete()
    return redirect('list')

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
