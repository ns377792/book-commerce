from django.urls import path 
from . import views

urlpatterns =[
    path('about/',views.aboutus, name='about'),
    path('privacypolicy/',views.privacy_policy, name='privacy_policy'),
    path('license/',views.licence, name='licence'),
    path('search', views.search_results, name='search'),

    
    
    
]