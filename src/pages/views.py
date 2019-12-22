from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import BookForm
from .models import Book


# Create your views here.
def home_view(request, *args, **kwargs):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
    else:
        user = None

    if user is not None:
        login(request, user)
        
    if request.user.is_authenticated:
        # Redirect to a success page.
        books = Book.objects.filter(author=request.user)
        return render(request, "home.html", {'username': request.user.username, 'books': books})
    else:
        return redirect('login') 

#def check_user(request):
#    if request.method == 'POST':
#        return redirect('home_view', username=request.POST['username'], password=request.POST['password'])

def log_in(request):
    return render(request, "login.html", {})

def log_out(request):
    logout(request)
    return redirect('home_view')

def test_user(request):
    form = BookForm(initial={'author': request.user})
    return render(request, 'test_user.html', {'form': form})

def new_book_item(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_view')