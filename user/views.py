# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from user.models import User, prereg
from user.hashmanager import makeHash
from user.hashmanager import is_valid_token
from user.hashmanager import generate_link_for_reset_pass


def profile(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == "POST":
        a = User.objects.filter(email=request.POST['email'])
        if a.count() == 1:
            a = a[0]
            if a.ban:
                return render(request, 'index.html', {'panel': 1, 'success': False, 'message': 'کاربر گرامی دستررسی شما قطع شده'})

            if a.is_valid_pass(request.POST['password']):
                request.session['login'] = True
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
                 password = makeHash('md5', request.POST['password'], request.POST['email'])).save()
            return render(request, 'index.html', {"mes": 'خوب به سلامتی ثبت نام شدی'})
    return render(request, 'index.html', {'mes': "ههههه ههههه ههههه"})


def password_change(request):
    return render(request, 'index.html')


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
                user_obj.password = request.POST['password']
                return render(request, 'password_reset_done.html', {'success': True})
            else:
                return render(request, 'password_reset_done.html', {'success': False})

    else:
        return render(request, 'password_reset_done.html', {'success': False})


def password_reset_complete(request):
    return render(request, 'index.html')
