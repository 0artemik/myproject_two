from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from datetime import datetime
from .models import Blog, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView



# регистрация
def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # Перенаправление после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'main/registration.html', {'form': form})




def about(request):
    return render(request, 'main/about.html')

def links(request):
    return render(request, 'main/links.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def pool(request):
    return render(request, 'main/pool.html')

from .forms import CommentForm, FeedbackForm



# форма обратной связи
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return render(request, 'main/thank_you.html', {'data': data})
    else:
        form = FeedbackForm()
    
    return render(request, 'main/pool.html', {'form': form})



# представление страницы блога
def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all().order_by('-posted')  # Получаем все статьи, сортируем по дате

    return render(
        request,
        'main/blog.html',
        {
            'title': 'Блог',
            'posts': posts,
            'year': datetime.now().year,
        }
    )

# получение статьи по id
#def blogpost(request, parametr):
#    """Renders the blogpost page."""
#    assert isinstance(request, HttpRequest)
#
#    post_1 = Blog.objects.get(id=parametr)  # Получаем статью по ID
#
#    return render(
#        request,
#        'main/blogpost.html',
#        {
#            'post_1': post_1,
#            'year': datetime.now().year,
#        }
#    )
def blogpost(request: HttpRequest, parametr):
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=post_1).order_by('-date')  # Сортируем по дате
    

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = post_1
            comment_f.save()
            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()

    return render(
        request,
        'main/blogpost.html',
        {
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )