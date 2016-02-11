from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from Blog.models import Article
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from forms import ArticleForm, LoginForm, SignupForm
from django.template import loader
from django.utils import timezone

 
class HomeView(TemplateView):
  template_name = 'index.html'
  


def index(request):
    
    latest_article_list = Article.objects.order_by('-post_date')[:5]
    form = ArticleForm()
    template = loader.get_template('index.html')
    context = {
        'form': form, 'posts': latest_article_list
    }
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            postedArticle = Article()
            postedArticle.post_date = timezone.now()
            postedArticle.title = request.POST.getlist('title')
            postedArticle.article = request.POST.getlist('article')
            postedArticle.save()
        else:
            form = ArticleForm(instance=article)
    return HttpResponse(template.render(context, request))
    
    
def article_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
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


def login(request):
    form = LoginForm()
    template = loader.get_template('login.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def signup(request):
    form = SignupForm()
    template = loader.get_template('signup.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))
    # TODO: write code...