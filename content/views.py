from django.shortcuts import render,redirect,get_object_or_404
from .models import Post

# Create your views here.
def list_(request):
    posts = Post.objects
    return render(request, 'list.html',{'posts':posts})

def main(request):
    pass

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
    return redirect('/content/detail/'+str(post_id))


def detail(request,post_id):
    onepost=get_object_or_404(Post,pk=post_id)
    return render(request,'detail.html',{'onepost':onepost})

def edit(request,post_id):
    onepost=get_object_or_404(Post,pk=post_id)
    return render(request,'edit.html',{'onepost':onepost})

def delete(request,post_id):
    deletepost=get_object_or_404(Post,pk=post_id)
    deletepost.delete()
    return redirect('list')



def new_comment(request, post_id):
    pass

def del_comment(request, comment_id):
    pass
