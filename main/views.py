from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, DetailView, UpdateView

from .forms import NewUserForm
from .models import News, Category


def home(request):
    first_news = News.objects.first()
    three_news = News.objects.all()[1:3]
    three_categories = Category.objects.all()[0:3]
    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news,
        'three_categories': three_categories
    })


# All News


def all_news(request):
    all_news = News.objects.all()
    return render(request, 'all-news.html', {
        'all_news': all_news
    })


# Detail Page


# Fetch all category


def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html', {
        'cats': cats
    })


# Fetch all category
def category(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'all_news': news,
        'category': category
    })


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="accounts/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


class DescriptionDelete(DeleteView):
    model = News
    context_object_name = 'home'
    success_url = reverse_lazy('home')


class DescriptionCreate(CreateView):
    model = News
    fields = ['detail', 'title', 'image', 'category']
    success_url = reverse_lazy('home')


class DescriptionDetail(DetailView):
    model = News


class DescriptionUpdate(UpdateView):
    model = News
    fields = ['name']
    success_url = reverse_lazy('home')

def simple_upload(request):
   if request.method == 'POST' and request.FILES['image']:
      image = request.FILES['image']