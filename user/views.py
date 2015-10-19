from django.shortcuts import render, render_to_response
from user.models import User


def index(request):
    return render(request, 'index.html')


def login(request):
    state = False
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.get(email=email).isValidPass(password):
            state = True

    return render(request, 'login.html', {'state': state})


def logout(request):
    return render(request, 'index.html')


def password_change(request):
    return render(request, 'index.html')


def password_change_done(request):
    return render(request, 'index.html')


def password_reset(request):
    return render(request, 'index.html')


def password_reset_done(request):
    return render(request, 'index.html')


def password_reset_complete(request):
    return render(request, 'index.html')
