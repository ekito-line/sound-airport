from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, User, Follow, Like
from .forms import PostForm, FollowForm, LikeForm

from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.


def home(request):
    return render(request, 'snsapp/home.html')

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = 'https://sound-airport.azurewebsites.net'  # this can be current domain
    return redirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

#投稿用の処理
# @login_required(login_url='/snsapp/login/')
def post(request):
    params = {
        'form': PostForm(),
    }

    if (request.method == 'POST'):
        title = request.POST['title']
        creator = request.user
        publish_date = date.today()
        post = Post(title = title, creator = creator, publish_date = publish_date)
        post.save()
        return redirect(to = '/main')
    return render(request, 'snsapp/post.html', params)

#Mainに投稿を表示する
# @login_required(login_url='/login/')
def main(request):
    user = request.user #これでuserが取れているのか不安。creatorかな
    posts = Post.objects.order_by('created_date')

    params = {
        'data' : posts,
        'user' : user,
    }

    return render(request, 'snsapp/main.html', params)

#followするための関数
# @login_required(login_url='/login/')
def follow(request, user_id):
    params = {
        'form' : FollowForm(),
    }

    follow_user = get_object_or_404(User, pk=user_id)

    if (request.method == 'POST'):
        creator = request.user
        follow_target = follow_user
        follow = Follow(creator = creator, follow_target = follow_target)
        follow.save()
        return redirect(to = '/main')

    return render(request, 'snsapp/main.html', params)

#Likeするための関数
# @login_required(login_url='/accounts/login/')
def like(request, post_id):
    params = {
        'form' : LikeForm(),
    }

    target_post = get_object_or_404(Post, pk=post_id)

    if (request.method == 'POST'):
        creator = request.user
        target_post = target_post
        like = Like(creator = creator, target_post = target_post)
        like.save()
        return redirect(to = '/main')

    return render(request, 'snsapp/main.html', params)
