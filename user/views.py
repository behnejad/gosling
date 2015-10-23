# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from user.models import User, prereg
from datetime import datetime
from user.hashmanager import makeHash

def home(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        a = User.objects.filter(email=request.POST['email'])
        if a.count() == 1:
            a = a[0]
            if a.ban:
                return render(request, 'index.html', {'panel': 1, 'fail': True, 'message': 'کاربر گرامی دستررسی شما قطع شده'})

            if a.isValidPass(request.POST['password']):
                request.session['login'] = True
                return HttpResponseRedirect('/home/')

    return render(request, 'index.html', {'panel': 1, 'fail': True, 'message': 'ورود با شکست مواجه شد'})


def logout(request):
    request.session.clear()
    return render(request, 'index.html', {'panel': 1, 'success': True, 'message': 'شما باموفقیت خارج شدید'})


def register(request):
    if request.method == "POST":
        if User.objects.filter(email=request.POST['email']).count() == 0:
            if prereg.objects.filter(mail=request.POST['email']).count() == 0:
                prereg(mail=request.POST['email'], smash=makeHash('md5', request.POST['email'])).save()
                return render(request, 'index.html', {'panel': 2, 'success': True, 'message': 'دوست عزیز برو میلتو چک کن'})
            return render(request, 'index.html', {'panel': 2, 'fail': True, 'message': 'دوست عزیز برو میلتو چک کن'})
        return render(request, 'index.html', {'panel': 2, 'fail': True, 'message': 'این ایمیل وجود داره انقد نزن'})
    return render(request, 'index.html', {'panel': 2, 'fail': True, 'message': 'ثبت نام با شکست مواجه شد'})


def forgot(request):
    if request.method == "POST":
        a = User.objects.filter(email=request.POST['email'])
        if a.count() == 1:
            a = a[0]
            if a.request:
                return render(request, 'index.html', {'panel': 3, 'fail': True, 'message': 'چند بار یه درخواست رو میدی'})

            a.request = True
            a.save()
            return render(request, 'index.html', {'panel': 3, 'success': True, 'message': 'دوست عزیز برو میلتو چک کن'})
        return render(request, 'index.html', {'panel': 3, 'fail': True, 'message': 'دوست عزیز همچین چیزی وجود نداره'})
    return render(request, 'index.html', {'panel': 3, 'fail': True, 'message': 'عملیات با شکست مواجه شد'})

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
