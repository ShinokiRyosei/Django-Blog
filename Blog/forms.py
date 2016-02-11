from django.forms import ModelForm
from Blog.models import Article, User


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
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)