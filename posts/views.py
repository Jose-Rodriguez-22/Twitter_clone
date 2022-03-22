from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.


def index(request):
    # if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # if the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()

            # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # No, show error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]

    # show
    return render(request, 'posts.html',
                  {'posts': posts})


def delete(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    newlikecount = Post.objects.get(id=post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES, instance=posts)
        # if the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()

            # Redirect to home
            return HttpResponseRedirect('/')

        else:
            # No, show error
            return HttpResponseRedirect('notvalid')
    return render(request, 'edit.html',
                  {'posts': posts})

    

    
    