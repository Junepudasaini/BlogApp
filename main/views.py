from django.core.exceptions import MultipleObjectsReturned
from django.shortcuts import redirect, render
from .models import Post
from .forms import CommentForm
# Create your views here.
def homepage(request):
    my_post = Post.objects.all()

    return render(request, 'main/homepage.html',{'my_post':my_post})

def detail(request, slug):
    post_detail = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post= post_detail
            comment.save()

            return redirect('detail', slug=post_detail.slug)
    else:
        form = CommentForm()            
  
    return render(request,'main/detail.html',{'post_detail':post_detail,'form':form})    