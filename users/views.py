from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('the_main-home')
    else:
        form = UserRegistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})
