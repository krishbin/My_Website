from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'krish',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'August 27,2020'
    },
    {
        'author': 'nads',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'August 27,2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
