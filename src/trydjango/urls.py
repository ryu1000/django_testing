"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import home_view, test_user, log_in, log_out, new_book_item
from products.views import create_view, run_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('<str:username>/<str:password>', home_view, name='home_view'),
    path('test-user', test_user, name='test-user'),
    path('new-book-item', new_book_item, name='new-book-item'),
    path('login', log_in, name='login'),
    path('logout', log_out, name='log-out'),
    path('create/', create_view, name='create_view'),
    path('run/', run_view, name='run_view')
]
