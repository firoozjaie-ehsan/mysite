from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # path('urladdresses', "view")
    path('',blog_view,name='index'),
    path('blog',blog_single,name='single'),
]
