from django.shortcuts import render, redirect
from .forms import UserRegistration, ProfileImage, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            f = User.objects.all()
            emaill = form.cleaned_data.get('email')
            for us in f:
                if us.email == emaill:
                    messages.error(request, f'Utilzatorul cu email-ul {us.email} exista')
                    return redirect('registration')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Utilzatorul {username} s-a creat cu succes')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'users/registration.html', {
        "form": form,
        "title": "Registration",
    })

@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)
        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Datele dvs. s-au modificat cu succes')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)
    dict = {
        'img_profile':img_profile,
        'update_user':update_user,
        "title":"Profile",
    }
    return render(request, 'users/profile.html', dict)
