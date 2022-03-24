# from socket import fromshare
from django import forms
from .models import Post, Follow, Like


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'icon',
            'title',
            'sound',
        )

class FollowForm(forms.Form):
    class Meta:
        model = Follow
        fields = ('creator', 'follow_target')

class LikeForm(forms.Form):
    class Meta:
        model = Like
        fields = ('creator', 'target_post')