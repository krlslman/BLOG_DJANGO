from django.shortcuts import render, redirect, get_object_or_404
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

def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    context = {
        "object": obj
    }
    return render(request, "blog/post_detail.html", context)

def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)  # instance brings the form filled with the data
    if form.is_valid():
        form.save()
        return redirect("blog:list")
    
    context = {
        "object": obj,
        "form": form,
        }
    return render(request, "blog/post_update.html", context)
    
def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        obj.delete()
        return redirect("blog:list")
    context = {
        "object": obj
    }
    return render(request, "blog/post_delete.html", context)