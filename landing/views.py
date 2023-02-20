from django.shortcuts import render, redirect
from .models import Post , Category
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.template import *
from django.http import JsonResponse


def homepage(request):
    allcat = Category.objects.all()
    p = Paginator(Post.objects.all().order_by("title"), 10)
    page= request.GET.get('page')
    blog_page = p.get_page(page)
    if 'term' in request.GET:
        qs = Post.objects.filter(title__icontains=request.GET.get('term'))
        titless= list()
        for postss in qs:
            titless.append(postss.title)
        return JsonResponse(titless, safe=False)     

    for cat in allcat:
        cat.link = cat.name.replace(' ', '-') 
    return render(request, 'home/homepage.html',  {'blog_page':blog_page, "allcats":allcat})



 
      

def detailpage(request, slug):
    post = Post.objects.get(slug = slug)
    return render(request, 'home/detailpage.html',  {'post':post, 'slug':post.slug})



class CatListView(ListView):
    template_name = 'home/categroy.html'
    context_object_name = 'catlist'
    

    def get_queryset(self):
        content = {
            'cat': self.kwargs['categroy'],
            'catpost' : Post.objects.filter(category__name=self.kwargs['categroy'])
        }
        return content

