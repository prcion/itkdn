from django.shortcuts import render
from .models import News
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

def home(request):
    news = News.objects.all().order_by('-date')
    n = news[1].nr
    n += 1
    news.update(nr=n)

    return render(request, "blog/home.html", {"news": news,
    "title":"Home",
    })

class ShowNewsList(ListView):
    model = News
    template_name = "blog/home.html"
    context_object_name = 'news'
    ordering = ['-date']
    def get_context_data(self, **kwards):
        ctx = super(ShowNewsList, self).get_context_data(**kwards)
        ctx['title'] = 'Home'
        return ctx

class NewsDetailView(DetailView):
    model = News
    template_name = "blog/news_detail.html"
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)
        ctx['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        news = News.objects.filter(pk=self.kwargs['pk'])
        n = news[0].nr
        n += 1
        news.update(nr=n)
        return ctx

@login_required
def contacts(request):
    return render(request, 'blog/test.html',{"title":"Test",})
