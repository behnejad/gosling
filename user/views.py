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



#Test for farsi encoding
#سلام هومن خیلی چیزی
#سلام امید کجایی؟!
#"وات د هل"

def login(request):
    if request.method == "POST":
        a = User.objects.filter(email=request.POST['email'])
        if a.count() == 1:
            a = a[0]
            if a.ban:
                return render(request, 'index.html', {'panel': 1, 'fail': True, 'message': 'ع©ط§ط±ط¨ط± ع¯ط±ط§ظ…غŒ ط¯ط³طھط±ط±ط³غŒ ط´ظ…ط§ ظ‚ط·ط¹ ط´ط¯ظ‡'})

            if a.isValidPass(request.POST['password']):
                request.session['login'] = True
                return HttpResponseRedirect('/home/')

    return render(request, 'index.html', {'panel': 1, 'fail': True, 'message': 'ظˆط±ظˆط¯ ط¨ط§ ط´ع©ط³طھ ظ…ظˆط§ط¬ظ‡ ط´ط¯'})


def logout(request):
    request.session.clear()
    return render(request, 'index.html', {'panel': 1, 'success': True, 'message': 'ط´ظ…ط§ ط¨ط§ظ…ظˆظپظ‚غŒطھ ط®ط§ط±ط¬ ط´ط¯غŒط¯'})


def register(request):
    if request.method == "POST":
        if User.objects.filter(email=request.POST['email']).count() == 0:
            if prereg.objects.filter(mail=request.POST['email']).count() == 0:
                prereg(mail=request.POST['email'], smash=makeHash('md5', request.POST['email'])).save()
                return render(request, 'index.html', {'panel': 2, 'success': True, 'message': 'ط¯ظˆط³طھ ط¹ط²غŒط² ط¨ط±ظˆ ظ…غŒظ„طھظˆ ع†ع© ع©ظ†'})
            return render(request, 'index.html', {'panel': 2, 'fail': True, 'message': 'ط¯ظˆط³طھ ط¹ط²غŒط² ط¨ط±ظˆ ظ…غŒظ„طھظˆ ع†ع© ع©ظ†'})
        return render(request, 'index.html', {'panel': 2, 'fail': True, 'message': 'ط§غŒظ† ط§غŒظ…غŒظ„ ظˆط¬ظˆط¯ ط¯ط§ط±ظ‡ ط§ظ†ظ‚ط¯ ظ†ط²ظ†'})
    return render(request, 'index.html', {'panel': 2, 'fail': True, 'message': 'ط«ط¨طھ ظ†ط§ظ… ط¨ط§ ط´ع©ط³طھ ظ…ظˆط§ط¬ظ‡ ط´ط¯'})


def forgot(request):
    if request.method == "POST":
        a = User.objects.filter(email=request.POST['email'])
        if a.count() == 1:
            a = a[0]
            if a.request:
                return render(request, 'index.html', {'panel': 3, 'fail': True, 'message': 'ع†ظ†ط¯ ط¨ط§ط± غŒظ‡ ط¯ط±ط®ظˆط§ط³طھ ط±ظˆ ظ…غŒط¯غŒ'})

            a.request = True
            a.save()
            return render(request, 'index.html', {'panel': 3, 'success': True, 'message': 'ط¯ظˆط³طھ ط¹ط²غŒط² ط¨ط±ظˆ ظ…غŒظ„طھظˆ ع†ع© ع©ظ†'})
        return render(request, 'index.html', {'panel': 3, 'fail': True, 'message': 'ط¯ظˆط³طھ ط¹ط²غŒط² ظ‡ظ…ع†غŒظ† ع†غŒط²غŒ ظˆط¬ظˆط¯ ظ†ط¯ط§ط±ظ‡'})
    return render(request, 'index.html', {'panel': 3, 'fail': True, 'message': 'ط¹ظ…ظ„غŒط§طھ ط¨ط§ ط´ع©ط³طھ ظ…ظˆط§ط¬ظ‡ ط´ط¯'})


def doreg(request):
    if request.method == 'GET' and request.GET.has_key('id') and request.GET.has_key('mail'):
        a = prereg.objects.filter(mail=request.GET['mail'], smash=request.GET['id'])
        if a.count():
            a[0].delete()
            return render(request, 'register.html', {'mail': request.GET['mail']})

    elif request.method == 'POST':
        print request.POST.has_key('firstname')
        print request.POST.has_key('lastname')
        print request.POST.has_key('email')
        print request.POST.has_key('password')

        if request.POST.has_key('firstname') and request.POST.has_key('lastname') and \
            request.POST.has_key('password') and request.POST.has_key('email'):
            User(first_name=request.POST['firstname'], last_name=request.POST['lastname'], email=request.POST['email'],
                 password=makeHash('md5', request.POST['password'], request.POST['email'])).save()
            return render(request, 'index.html', {"mes": 'ط®ظˆط¨ ط¨ظ‡ ط³ظ„ط§ظ…طھغŒ ط«ط¨طھ ظ†ط§ظ… ط´ط¯غŒ'})
    return render(request, 'index.html', {'mes': "ظ‡ظ‡ظ‡ظ‡ظ‡ ظ‡ظ‡ظ‡ظ‡ظ‡ ظ‡ظ‡ظ‡ظ‡ظ‡"})



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
