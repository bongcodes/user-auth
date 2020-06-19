from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import get_user_model, authenticate, login, logout


def signup_view(request, *args, **kwargs):
    # form = UserCreationForm(request.POST or None)
    form = UserRegisterForm(request.POST or None)
    template_name = 'accounts/register.html'

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('pages:index')

    context = {'form': form}
    return render(request, template_name, context)


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    templete_name = 'accounts/login.html'

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            if next:
                return redirect(next)
            return redirect('pages:index')
    return render(request, templete_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('pages:index')

