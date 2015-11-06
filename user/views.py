# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from user.models import User, prereg
from user.hashmanager import makeHash
from user.hashmanager import is_valid_token
from user.hashmanager import generate_link_for_reset_pass
import datetime


def profile(request):
    return render(request, 'profile.html')


def close(request):
    request.session.flush()
    return HttpResponseRedirect('/')


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        a = User.objects.filter(email=request.POST['email'])
        if a.count() == 1:
            a = a[0]
            if a.ban:
                return render(request, 'index.html', {'panel': 1, 'success': False, 'message': 'کاربر گرامی دستررسی شما قطع شده'})

            if a.is_valid_pass('md5', request.POST['password']):
                request.session['login'] = True
                request.session['email'] = a.email
                request.session['first_name'] = a.first_name
                return HttpResponseRedirect('/home/')

    return render(request, 'index.html', {'panel': 1, 'success': False, 'message': 'ورود با شکست مواجه شد'})


def logout(request):
    request.session.clear()
    return render(request, 'index.html', {'panel': 1, 'success': True, 'message': 'شما باموفقیت خارج شدید'})


def register(request):
    if request.method == "POST":
        if User.objects.filter(email=request.POST['email']).count() == 0:
            if prereg.objects.filter(mail=request.POST['email']).count() == 0:
                prereg(mail=request.POST['email'], smash=makeHash('md5', request.POST['email'])).save()
                return render(request, 'index.html', {'panel': 2, 'success': True, 'message': 'دوست عزیز برو میلتو چک کن'})
            return render(request, 'index.html', {'panel': 2, 'success': False, 'message': 'دوست عزیز برو میلتو چک کن'})
        return render(request, 'index.html', {'panel': 2, 'success': False, 'message': 'این ایمیل وجود داره انقد نزن'})
    return render(request, 'index.html', {'panel': 2, 'success': False, 'message': 'ثبت نام با شکست مواجه شد'})


def forgot(request):
    if request.method == "POST":
        a = User.objects.filter(email=request.POST['email'])
        if a.count() == 1:
            a = a[0]
            if a.request:
                return render(request, 'index.html', {'panel': 3, 'success': False, 'message': 'چند بار یه درخواست رو میدی'})

            a.request = True
            a.save()
            generate_link_for_reset_pass(a)
            return render(request, 'index.html', {'panel': 3, 'success': True, 'message': 'دوست عزیز برو میلتو چک کن'})
        return render(request, 'index.html', {'panel': 3, 'success': False, 'message': 'دوست عزیز همچین چیزی وجود نداره'})
    return render(request, 'index.html', {'panel': 3, 'success': True, 'message': 'عملیات با شکست مواجه شد'})


def do_reg(request):
    if request.method == 'GET' and request.GET.get('id') and request.GET.get('mail'):
        a = prereg.objects.filter(mail=request.GET['mail'], smash=request.GET['id'])
        if a.count():
            a[0].delete()
            return render(request, 'register.html', {'mail': request.GET['mail']})

    elif request.method == 'POST':

        if request.POST.get('firstname') and request.POST.get('lastname') and \
            request.POST.get('password') and request.POST.get('email'):
            User(first_name=request.POST['firstname'], last_name=request.POST['lastname'], email=request.POST['email'],
                 password=makeHash('md5', request.POST['password'].encode('utf-8'), request.POST['email'].encode('utf-8')),
                 datecreate=datetime.now()).save()
            return render(request, 'index.html', {"mes": 'خوب به سلامتی ثبت نام شدی'})
    return render(request, 'index.html', {'mes': "ههههه ههههه ههههه"})


def password_change(request):
    if request.method == 'POST':
        if request.POST.get('password'):
            a = User.objects.filter(email=request.session['email'])
            if len(a) > 0:
                a = a[0]
                a.password = makeHash('md5', request.POST.get('password').encode('utf-8'), request.session['email'].encode('utf-8'))
                a.save()
                return HttpResponseRedirect('/home?mes=1')
    return HttpResponseRedirect('/home?mes=0')


def password_change_done(request):
    return render(request, 'index.html')


def password_reset(request):
    if request.GET.has_key('token') and request.GET.has_key('user_id'):
        token = request.GET['token']
        user_id = request.GET['user_id']
        return render(request, 'pass_reset.html', {'success': True, 'token': token, 'user_id': user_id})
    return render(request, 'pass_reset.html', {'success': False})


def password_reset_done(request):
    if request.POST.has_key('password') and request.POST.has_key('password2') and request.POST.has_key('token') and request.POST.has_key('user_id'):
        try:
            user_obj = User.objects.get(id=request.POST['user_id'])
        except User.DoesNotExist:
            return render(request, 'password_reset_done.html', {'success': False})
        else:
            if is_valid_token(request.POST['token'], user_obj) and request.POST['password'] == request.POST['password2']:
                #user_obj.password = request.POST['password']
                user_obj.password = makeHash('md5', request.POST['password'].encode("utf8"), user_obj.email.encode("utf8"))
                user_obj.save()

                return render(request, 'password_reset_done.html', {'success': True})
            else:
                return render(request, 'password_reset_done.html', {'success': False})

    else:
        return render(request, 'password_reset_done.html', {'success': False})


def password_reset_complete(request):
    return render(request, 'index.html')


def group(request):
    return render(request, 'index.html')
