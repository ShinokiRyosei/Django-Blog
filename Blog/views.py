from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from Blog.models import Article, User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from forms import ArticleForm, LoginForm, SignupForm
from django.template import RequestContext
from django.template import loader
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

 
class HomeView(TemplateView):
  template_name = 'index.html'
  

def index(request):
    latest_article_list = Article.objects.all().order_by('-post_date')[:5]
    form = ArticleForm()
    template = loader.get_template('index.html')
    # user = User.objects.get(pk=User.pk)
    if request.user.is_active:
    # if user is not None:
        
        return render_to_response('index.html', { 'form': form, 'posts': latest_article_list })
    elif request.user.is_active != False and latest_article_list is not None:
        return render_to_response('index.html', { 'posts': latest_article_list })
        
    else:
        return render_to_response('index.html', {  }, context_instance=RequestContext(request))
        
    if request.method == 'POST':
        if form.is_valid():
            postedArticle = Article()
            postedArticle.post_date = timezone.now()
            postedArticle.title = request.POST.getlist('title')
            postedArticle.article = request.POST.getlist('article')
            postedArticle.save()
        else:
            form = ArticleForm(instance=article)
    return render_to_response('index.html', { 'form': form, 'posts': latest_article_list }, context_instance=RequestContext(request))
    
    
def article_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, )
        if form.is_valid():
            postedArticle = Article()
            postedArticle.post_date = timezone.now()
            postedArticle.title = request.POST.getlist('title')
            postedArticle.article = request.POST.getlist('article')
            postedArticle.save()
    
            # return redirect('index')
    else:
        form = ArticleForm(instance=article)
        
    return render_to_response('post_article.html', dict(form=form), context_instance=RequestContext(request))


# def login(request):
#     form = LoginForm()
#     template = loader.get_template('login.html')
#     context = {
#         'form': form
#     }
#     if request.method == 'POST':
#         user = authenticate(username=request.POST.getlist('username'), password=request.POST.getlist('password'))
#         if user.is_active():
#         login(request, user)
#         return redirect('https://django-blog-shinokin.c9users.io/')
#                 # return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
#     return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


def signup(request):
    user = User()
    form = SignupForm()
    template = loader.get_template('signup.html')
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = SignupForm(request.POST, instance=user)
        if form.is_valid:
            new_user = form.save()
            # postedSignup = User
            # postedSignup.username = request.POST.getlist('username')
            # postedSignup.email = request.POST.getlist('email')
            # postedSignup.password = request.POST.getlist('password')
            # postedSignup.save()
            return redirect('https://django-blog-shinokin.c9users.io/')
            # return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
    return render_to_response('signup.html', {'form': form}, context_instance=RequestContext(request))
    # TODO: write code...