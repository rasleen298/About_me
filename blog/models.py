from django.db import models

# Create your models here.
class Blog(models.Model):
    #title
    #pub_date
    #body
    #images
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
