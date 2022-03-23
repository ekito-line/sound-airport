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
        return redirect(to = '/followinglist')

    return render(request, 'snsapp/followinglist.html', params)

def mypage(request):
    #follow数を数える
    follows = Follow.objects.all()
    posts = Post.objects.all()
    
    #database上のcreatorが自分の数を数える→フォロー数
    follow_list = []
    for follow in follows:
        if follow.creator == request.user:
            follow_list.append(1)
    follow_num = len(follow_list)

    #database上のfollow_targetが自分の数を数える→フォロワー数
    follower_list = []
    for follower in follows:
        if follower.follow_target == request.user:
            follower_list.append(1)
    follower_num = len(follower_list)

    #自分が投稿者の投稿の数を数える
    post_list = []
    for post in posts:
        if post.creator == request.user:
            post_list.append(1)
    post_num = len(post_list)

    #自分の投稿だけに絞る
    mypost = Post.objects.filter(creator = request.user)

    #私はだれか
    user_name = request.user

    params = {
        'user_name' : user_name,
        'follow_num' : follow_num,
        'follower_num' : follower_num,
        'post_num' : post_num,
        'mypost' : mypost,
    }

    return render(request, 'snsapp/mypage.html', params)

def followinglist(request):
    #follow数を数える
    follows = Follow.objects.all()
    
    #database上のcreatorが自分の数を数える→フォロー数
    follow_list = []
    for follow in follows:
        if follow.creator == request.user:
            follow_list.append(1)
    follow_num = len(follow_list)

    #database上のfollow_targetが自分の数を数える→フォロワー数
    follower_list = []
    for follower in follows:
        if follower.follow_target == request.user:
            follower_list.append(1)
    follower_num = len(follower_list)

    #私はだれか
    user_name = request.user

    #自分がフォローしているユーザー
    follow = Follow.objects.filter(creator = request.user)

    #自分のフォロワー
    follower = Follow.objects.filter(follow_target = request.user)


    if request.method == 'POST':
        if 'button_1' in request.POST:
            # ボタン1がクリックされた場合の処理
            params = {
                'user_name' : user_name,
                'follow_num' : follow_num,
                'follower_num' : follower_num,
                'follow' : follow,
            }
            return render(request, 'snsapp/followinglist.html', params)
        elif 'button_2' in request.POST:
            # ボタン2がクリックされた場合の処理
            params = {
                'user_name' : user_name,
                'follow_num' : follow_num,
                'follower_num' : follower_num,
                'follower' : follower,
            }
            return render(request, 'snsapp/followinglist.html', params)


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
