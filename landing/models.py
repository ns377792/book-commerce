from django.db import models
from tinymce import models as tinymce_models

   


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name  

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    author_name = models.CharField(max_length=255, blank=True, null=True)
    sale_price = models.CharField(max_length=55, blank=True, null=True)
    price = models.CharField(max_length=55, blank=True, null=True)
    body = tinymce_models.HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    featured_img = models.ImageField(upload_to="blog/featured_img", blank=True, null=True)
    main_img = models.ImageField(upload_to="blog/main_img",  blank=True, null=True)
    date_added = models.DateField(auto_now=True)
    
    def __str__(self):
         return self.title


    class Meta:
        ordering =['-date_added']



    
