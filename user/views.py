# from cProfile import Profile
from email import message
from django.shortcuts import redirect, render,redirect
from .form import UserRegisteForm,ProfileForm
from django.contrib import messages
from .models import Profile
from django.contrib.auth.decorators import login_required


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = UserRegisteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Registration successful')
            return redirect('user_login')
        else:
            messages.error(request, "Username already exists or Email.Please Login to your Account!")
    form = UserRegisteForm()
    context = {
        'form':form,
    }
    return render(request, 'user/register.html',context)


@login_required(login_url='user_login')
def profile(request):
    user = request.user
    profile = Profile.objects.filter(user__username = user).first()
    print(profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        
        if form.is_valid():
            profile_instance = form.save(commit = False)
            profile_instance.user = user
            profile_instance.save()
            messages.info(request, "Your profile has been updated Successfully")
            return redirect('profile')
    form = ProfileForm(instance = profile)
    context = {
        "form":form,
        "profile":profile,
    }
    return render(request,'user/profile.html', context)

