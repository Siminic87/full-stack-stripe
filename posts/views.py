from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Post, Voter
from django.contrib.auth.models import User
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def get_posts(request):
    """
    Create a view that will return a list
    of Bugs that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(type="Bug", published_date__lte=timezone.now()
        ).order_by('-upvotes')
    return render(request, "blogposts.html", {'posts': posts})
    
def get_features(request):
    """
    Create a view that will return a list
    of Feature Requests that were published prior to 'now'
    and render them to the 'features.html' template
    """
    posts = Post.objects.filter(type="Feature Request", published_date__lte=timezone.now()
        ).order_by('-upvotes')
    return render(request, "features.html", {'posts': posts})

def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})
    
@login_required()
def upvote(request, post_id):
    
    if Voter.objects.filter(post_id=post_id, user_id=request.user.id).exists():

        messages.info(request, 'You already upvoted this!')
        return redirect(reverse('get_posts'))

    else:
        post = get_object_or_404(Post, pk=post_id)
        post.upvotes += 1
        post.save()
        Voter.objects.create(post_id=post_id, user_id=request.user.id)
        
    return redirect(reverse('get_posts'))
    
@login_required()
def upvote_feature(request, post_id):
    
    if Voter.objects.filter(post_id=post_id, user_id=request.user.id).exists():

        messages.info(request, 'You already upvoted this!')
        return redirect(reverse('get_posts'))

    else:
        post = get_object_or_404(Post, pk=post_id)
        post.upvotes += 1
        post.save()
        Voter.objects.create(post_id=post_id, user_id=request.user.id)
        
    return redirect(reverse('get_posts'))

def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})