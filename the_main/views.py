from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *

def apartment(request):

    if request.method == "POST":
        form = apartmentForm(request.POST or None)
        if form.is_valid():
             blog_item = form.save(commit=True)
             blog_item.save()
        return render(request, 'the_main/apartment.html', {'form': form}, {'form': apartment, 'title': 'Квартиры'})
    else:
        form = apartmentForm()
    return render(request, 'the_main/apartment.html', {'form': form}, {'form': apartment, 'title': 'Квартиры'})

def rental(request):

    rental = rentalForm(request.POST)
    return render(request, 'the_main/rental.html', {'form': rental, 'title': 'Аренда'}, locals)

def home(request):

    form = SubscribersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        username = form.cleaned_data.get('username')
        messages.success(request, f'Пользователь {username} был успешно зарегистрирован!')
        new_form = form.save()
        return redirect('the_main-home')
    
    return render(request, 'the_main/home.html', {'form': form, 'title': 'Главная страница'})

def contacti(request):
    return render(request, 'the_main/contacti.html', {'title': 'Страничка контакты'})

def site(request):
    return render(request, 'the_main/site.html', {'title': 'site'})

