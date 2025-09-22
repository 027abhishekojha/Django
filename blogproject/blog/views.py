from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import comment

from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()  # Query the database for all posts
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

@login_required
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        comment_text = request.POST.get('text')
        Comment.objects.create(
            post=post,
            text=comment_text,
        )
        return redirect('post_details', pk=pk)


    comments = post.comment_set.all()
    # comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/post_details.html', context)