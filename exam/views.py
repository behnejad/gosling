from django.shortcuts import render, render_to_response
from exam.models import field, section, problem as prob


def index(request):
    return render(request, 'index.html')


def exam(request, eID):
    return render(request, 'index.html')


def exam_list(request):
    return render(request, 'index.html')


def group(request, eID):
    return render(request, 'index.html')


def group_list(request):
    return render(request, 'index.html')


def problem(request):
    return render(request, 'problem.html')


def createGroup(request):
    return render(request, 'group_create_login.html', {'create': True})


def loginGroup(request):
    return render(request, 'group_create_login.html', {'create': False})


def add_problem(request):
    if request.POST.get('type'):
        return render(request, 'section.html', {'next': 'stat', 'data': section.objects.filter(fname=request.POST.get('type'))})

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



