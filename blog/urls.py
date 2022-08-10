from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # path('urladdresses', "view")
    path('',blog_view,name='index'),
    path('<int:pid>',blog_single,name='single'),
    # path('test',test,name='test')
    # path('<int:id>',blog_single,name='single')
]
