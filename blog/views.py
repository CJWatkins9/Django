from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Chris Watkins',
        'title': 'Blog post 1',
        'content': 'First post ever',
        'date': 'October 4th 2019'
    },
    {'author': 'Nick',
        'title': 'Blog post 2',
        'content': 'Second post ever',
        'date': 'October 3th 2019'
        }

]

def home (request):
    context = {'posts':posts}
    return render(request,'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})

