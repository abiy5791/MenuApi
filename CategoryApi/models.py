from django.db import models

class category(models.Model):
    cat_name = models.TextField()
    cat_image = models.TextField()
    cat_desc = models.TextField()
    updated_in = models.DateTimeField(auto_now=True)
    created_in = models.DateTimeField(auto_now_add=True)