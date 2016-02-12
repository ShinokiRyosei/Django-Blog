from django.forms import ModelForm
from Blog.models import Article, User
from django import forms


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'article',)
        
form = ArticleForm()


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        
        
class SignupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)