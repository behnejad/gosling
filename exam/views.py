# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from exam.models import field, section, problem as prob
from user.models import User, group as Group, group_user_relation
from datetime import datetime
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def exam(request, eID):
    return render(request, 'index.html')


def exam_list(request):
    return render(request, 'index.html')


def admin(request, gId):
    g = Group.objects.get(id=gId)
    if request.session['userId'] == g.admin_id:
        print group_user_relation.objects.filter(group=gId, user=request.POST['user']).delete()

    return HttpResponseRedirect('/exam/group/%s' % gId)


def group(request, eID):
    g = Group.objects.get(id=eID)
    if request.session['userId'] == g.admin_id:
        use = False
    else:
        use = True
    mems = group_user_relation.objects.filter(group=eID)
    return render(request, 'group.html', {'group': g, 'mems': mems, 'user': use})


def group_list(request):
    return render(request, 'groupList.html', {'list': Group.objects.get_queryset()})


def problem(request):
    p = prob.objects.get_queryset()[:1][0]
    return render(request, 'problem.html', {'problem': p})


def createGroup(request):
    if request.method == 'GET':
        return render(request, 'group_create_login.html', {'create': True,
                                                           'admin': User.objects.get(id=request.session['userId'])})

    else:
        a = User.objects.get(id=request.session['userId'])
        Group(name=request.POST['name'], admin=a, description=request.POST['description'],
              date_created=datetime.now(), password=request.POST['password']).save()
        return render(request, 'group_create_login.html', {'create': True, 'admin': a, 'mess': 'گروه با موفقیت ساخته شد'})


def loginGroup(request, gId):
    if request.method == 'POST':
        if group_user_relation.objects.filter(user=request.session['userId'], group=gId)[:1].count():
            return render(request, 'group_create_login.html', {'create': False, 'group': Group.objects.get(id=gId),
                                                               'mess': 'الان تو گروهی مگه مریضی؟'})

        g = Group.objects.get(id=gId)
        if g.password == request.POST['password']:
            group_user_relation(user=User.objects.get(id=request.session['userId']), group=g).save()
            return render(request, 'group_create_login.html', {'create': False, 'group': Group.objects.get(id=gId),
                                                                   'mess': 'در گروه ثبت نام شدی'})
        else:
            return render(request, 'group_create_login.html', {'create': False, 'group': Group.objects.get(id=gId),
                                                                   'mess': 'رمز اشتباهههه'})

    return render(request, 'group_create_login.html', {'create': False, 'group': Group.objects.get(id=gId)})

def add_problem(request):
    if request.POST.get('type'):
        return render(request, 'section.html', {'next': 'stat', 'data': section.objects.filter(fname=request.POST.get('type')),
                                                'd2': field.objects.get(id=request.POST.get('type'))})

    elif request.POST.get('stat'):
        return render(request, 'addproblem.html', {'state': request.POST.get('stat')})

    elif request.POST.get('final'):
        prob(sec=section.objects.get(id=request.POST.get('index')), text=request.POST.get('text'),
             question=request.POST.get('question'), answers=request.POST.get('answers')).save()
        return render(request, 'ok.html')

    else:
        return render(request, 'section.html', {'next': 'type', 'data': field.objects.get_queryset()})

def problem_list(request):
    return render(request, 'index.html')



