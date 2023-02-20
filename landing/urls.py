from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('<slug:slug>/', views.detailpage, name="detailpage"),
    path('category/<categroy>', views.CatListView.as_view() , name="categroy" ),
    
    
    
    
    

]