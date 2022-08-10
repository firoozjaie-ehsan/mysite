from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):

    image=models.ImageField(upload_to='blog/',default="blog/default.jpg")
    title=models.CharField(max_length=255)
    content=models.TextField()
    #tag
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    counted_view=models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    create_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_date']
        # verbose_name= "پست"
        # verbose_name_plural= "پست ها"

    def __str__(self):
        return "{}-{}".format(self.title,self.id)
        
    def incrementViewCount(self):
        self.counted_view += 1
        self.save()
