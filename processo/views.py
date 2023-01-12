from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ProcessoForm


def login_view(request):
    if request.method == "POST":
        username=request.POST.get('username',None)
        password=request.POST.get('password', None)
        validUser = authenticate(request,
            username=username,
            password=password
        )
        if validUser:
            login(request, validUser)
        else:
            messages.error(request, 'Credencias Incorretas')
        return redirect(reverse('processo:home-page'))
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('processo:home-page'))
        return render(request, 'login.html')



def home_page_view(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect(reverse('processo:login-page'))
    
def processo_render_form(request):
    form = ProcessoForm()
    return render(request,'processo_form.html', {
        'form': form
    })