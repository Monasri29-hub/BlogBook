from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def test(request):
    return render(request, 'blog/base.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'blog/user_login.html', {'error': 'Invalid username or password'})
    return render(request, 'blog/user_login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        if User.objects.filter(username=username).exists():
            return render(request, 'blog/signup.html', {
                'error': 'Username already exists. Please choose another.'
            })

        newUser = User.objects.create_user(username = username, email = email, password = password)
        newUser.save()
        return redirect('/login')
    return render(request, 'blog/signup.html')

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def newpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        newPost = models.Post(title=title, content=content, author=request.user)
        newPost.save()
        return redirect('/home')
    return render(request, 'blog/newpost.html')

def myposts(request):
    context = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'blog/mypost.html', context)

def signout(request):
    logout(request)
    return redirect('/login')
