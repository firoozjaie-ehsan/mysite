from django.shortcuts import render,get_object_or_404
import datetime
from blog.models import Post
from django.utils import timezone
# from next_prev import next_in_order, prev_in_order

# Create your views here.

def blog_view(request):
    # end_date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    # posts=Post.objects.filter(published_date__range=(Post.published_date.strftime("%Y-%m-%d %H:%M:%S"), end_date))
    
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1).order_by('-create_date')
    # default ordering

    post=get_object_or_404(Post,pk=pid,status=1)
    prev=None
    next=None
    flag=0
    for p in posts:
        if p!=post and flag==0:
            prev=p
        elif p==post:
            flag=1
        elif flag==1:
            next=p
            break
    post.incrementViewCount()
    context={'post':post,'prev':prev,'next':next}
    return render(request,'blog/blog-single.html',context)





# def test(request):
#     posts=get_list_or_404(Post,pk=pid)
#     context={'posts':posts}
#     return render(request,'blog/test.html',context)