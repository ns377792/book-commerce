from re import search
import re
from django.http import JsonResponse
from django.shortcuts import render
from .models import Aboutus, Privacy, Licence
from landing.models import Post
from django.core.paginator import Paginator

def aboutus(request):
    abouts= Aboutus.objects.get()
    return render(request, 'about.html',{'abouts':abouts})

def privacy_policy(request):
    pp_text= Privacy.objects.get()
    return render(request, 'pp.html',{'pp_text':pp_text})


def licence(request):
    licence_text= Licence.objects.get()
    return render(request, 'license.html',{'licence_text':licence_text})        

 

def search_results(request):
    if request.method == "POST":
        search = request.POST['search']
        search_results = Post.objects.filter(title__icontains=search)


    return render(request, 'search.html', {'search':search, 'search_results':search_results})    



def withcodes(request):
    p = Paginator (Post.objects.filter(with_code=True), 4)
    page = request.GET.get('page')
    f_post = p.get_page(page)
    return render(request, 'themes.html', {'f_post':f_post})