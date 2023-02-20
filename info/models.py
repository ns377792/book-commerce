from django.db import models
from tinymce import models as tinymce_models

class Aboutus(models.Model):
    about_text = tinymce_models.HTMLField() 


class Privacy(models.Model):
    privacy_text = tinymce_models.HTMLField() 


class Licence(models.Model):
    license_text = tinymce_models.HTMLField()         

