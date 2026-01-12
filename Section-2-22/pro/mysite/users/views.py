from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

def register(request):

    if request.method=="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, you have successfully logged in!')

            return redirect('login')
    
    form = RegisterForm()

    context = {
        'form':form
    }
    return render(request, 'users/register.html',context)



def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')
