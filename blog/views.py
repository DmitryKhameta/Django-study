from django.shortcuts import render
from blog.models import Post


posts = [
    {
        "author": "Max",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "Feb 25, 2022"
    },
    {
        "author": "Ian",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "Feb 23, 2022",
    }
]


def home(request):
    context = {
         "posts": Post.objects.all()
    }
    return render(request, "blog/index.html", context)


def about(request):
    return render(
        request,
        "blog/about.html",
        {
            "title": "About",
        }

    )
