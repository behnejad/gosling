# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from exam.models import field, section, problem as prob
from user.models import User, group as Group
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def exam(request, eID):
    return render(request, 'index.html')


def exam_list(request):
    return render(request, 'index.html')


def group(request, eID):
    return render(request, 'index.html')


def group_list(request):
    return render(request, 'groupList.html', {'list': Group.objects.get_queryset()})


def problem(request):
    p = prob.objects.get_queryset()[:1][0]
    return render(request, 'problem.html', {'problem': p})


def group(request):
    return render(request, 'group.html')


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
    if gId == 0:
        #TODO Login
        pass

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



