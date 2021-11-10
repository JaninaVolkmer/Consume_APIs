from django.shortcuts import render
from blog.forms import CommentForm
from blog.models import Post, Comment
# Create your views here.
"""
Create 3 view functions
:blog_index: will display a list of all your posts
:blog_detail: will display the full post as well as comments and a form to
allow users to create new comments
:blog_category: similar to blog_index, but posts viewed will only be of a
specific category chosen by the user
Django Queryset filter:
https://docs.djangoproject.com/en/2.1/topics/db/queries/#retrieving-
specific-objects-with-filters
"""


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        'created_on'
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    # create instance of form class
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # if form is valid, a new instance of Comment is created
        # access the data from the form using form.cleaned_data = dictionary
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)
