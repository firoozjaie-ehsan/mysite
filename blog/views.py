from django.shortcuts import render,get_object_or_404
import datetime
from blog.models import Post
from django.utils import timezone
# Create your views here.

def blog_view(request):
    # end_date = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    # posts=Post.objects.filter(published_date__range=(Post.published_date.strftime("%Y-%m-%d %H:%M:%S"), end_date))
    
    #منظور اگه پستهایی که تا الان منتظر شدن نمایش بده هست فک کنم جواب اینه اگه نده نتونستم جواب پیدا کنم
    posts=Post.objects.filter(published_date__lte=timezone.now())
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):

    post=get_object_or_404(Post,pk=pid,status=1)
    post.incrementViewCount()
    context={'post':post}
    return render(request,'blog/blog-single.html',context)





# def test(request):
#     posts=get_list_or_404(Post,pk=pid)
#     context={'posts':posts}
#     return render(request,'blog/test.html',context)