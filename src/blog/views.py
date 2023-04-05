from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def post_list(request):  # to list our post on the page
    # qs = Post.objects.all()
    qs = Post.objects.filter(status='p')  
    context = {
        "object_list": qs
    }
    return render(request, "blog/post_list.html", context)

def post_create(request):
    # Short way:
    # forms = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # do these since we only want the user to be able to select themselves as the author for their post
            post = form.save(commit=False)  # save but dont send to db yet
            post.author = request.user  # set author
            post.save()  # now save and send db
            return redirect("blog:list")  # in urls.py > app_name : path name
    context = {
        'form': form
    }
    return render(request, "blog/post_create.html", context)