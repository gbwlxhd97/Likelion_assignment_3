from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .form import BlogPost
def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    details = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html', {'details':details})

def new(request):
    return render(request,'new.html')

def create(request): #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body'] 
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    #

def blogpost(request):
    #입력된 내용을 처리하는기능 ->POST
    #빈 페이지를 띄워주는 기능  ->GET
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html',{'form':form})