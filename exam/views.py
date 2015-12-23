# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from exam.models import field, section, problem as prob, exam as examination, examproblems, useranswers
from user.models import User, group as Group, group_user_relation
from datetime import datetime
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def exam(request, eID):
    return render(request, 'exam.html', {'probs': examproblems.objects.filter(examid=eID),
                                         'exam': examination.objects.filter(id=eID)})


def exam_list(request):
    return render(request, 'index.html')


def admin(request, gId):
    g = Group.objects.get(id=gId)
    if request.session['userId'] == g.admin_id:
        print group_user_relation.objects.filter(group=gId, user=request.POST['user']).delete()

    return HttpResponseRedirect('/exam/group/%s' % gId)


def group(request, eID):
    g = Group.objects.get(id=eID)
    use = False if request.session['userId'] == g.admin_id else True
    mems = group_user_relation.objects.filter(group=eID)
    return render(request, 'group.html', {'group': g, 'mems': mems, 'user': use})


def group_list(request):
    return render(request, 'groupList.html', {'list': Group.objects.get_queryset()})


def problem(request):
    if request.GET.get('id'):
        p = prob.objects.filter(id=request.GET.get('id'))[0]
    else:
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
        # return render(request, 'group_create_login.html', {'create': True, 'admin': a, 'mess': 'گروه با موفقیت ساخته شد'})
        return HttpResponseRedirect('/profile/')

def loginGroup(request, gId):
    if request.method == 'POST':
        if group_user_relation.objects.filter(user=request.session['userId'], group=gId)[:1].count():
            return render(request, 'group_create_login.html', {'create': False, 'group': Group.objects.get(id=gId),
                                                               'mess': 'الان تو گروهی مگه مریضی؟'})

        g = Group.objects.get(id=gId)
        if g.password == request.POST['password']:
            group_user_relation(user=User.objects.get(id=request.session['userId']), group=g).save()
            return HttpResponseRedirect('/profile/')
            # return render(request, 'group_create_login.html', {'create': False, 'group': Group.objects.get(id=gId),
            #                                                        'mess': 'در گروه ثبت نام شدی'})
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
             question=request.POST.get('question'), answers=request.POST.get('answers'),
             correctanswer=request.POST.get('answe')).save()
        return render(request, 'ok.html')

    else:
        return render(request, 'section.html', {'next': 'type', 'data': field.objects.get_queryset()})

def problem_list(request):
    return render(request, 'index.html')

# Warning: Should only be used with AJAX or something similar
def answer_question(request):
    useri = request.POST.get('user')
    exami = request.POST.get('exam')
    problemi = request.POST.get('problem')
    answeri = request.POST.get('answer')
    if (useri and exami and problemi and answeri):
        t = examination.objects.filter(examid=exami)[:1]
        if t.count() and group_user_relation.objects.filter(user=useri, group=t[0].groupid)[:1].count() and examproblems.objects.filter(examid=exami, problemid=problemi)[:1].count():
            u = useranswers.objects.filter(userid=useri, examid=exami, problemid=problemi)
            if (u.count()):
                pass
                #useranswers.objects.get(userid=useri, examid=exami, problemid=problemi)
                #update the answer
            else:
                useranswers(userid=useri, examid=exami, problemid=problemi, answer=answeri).save()
            return render(request, 'ok.html')


def answer_questions(request):
    userin = request.POST.get('user')
    examin = request.POST.get('exam')
    problemin = request.POST.get('problem')
    answern = request.POST.get('answer')
    if (userin and examin and problemin and answern):
        for i in range(len(userin)):
            useri = userin[i]
            exami = examin[i]
            problemi = problemin[i]
            answeri = answern[i]
            
            t = examination.objects.filter(examid=exami)[:1]
            if t.count() and group_user_relation.objects.filter(user=useri, group=t[0].groupid)[:1].count() and examproblems.objects.filter(examid=exami, problemid=problemi)[:1].count():
                u = useranswers.objects.filter(userid=useri, examid=exami, problemid=problemi)
                if (u.count()):
                    pass
                    #useranswers.objects.get(userid=useri, examid=exami, problemid=problemi)
                    #update the answer
                else:
                    useranswers(userid=useri, examid=exami, problemid=problemi, answer=answeri).save()
    return render(request, 'profile.html')


def create_exam(request):
    gr = request.POST.get('group')
    sd = request.POST.get('startdate')
    ed = request.POST.get('enddate')
    nm = request.POST.get('name')
    
    if (gr and sd and ed and nm):
        examination(groupid=gr, startdate=sd, enddate=ed, name=nm).save()
        return render(request, 'examaddproblems.html')
    return render(request, 'profile.html')
    
# AJAX???
def add_problem_to_exam(request):
    exid = request.POST.get('exam')
    prid = request.POST.get('problem')
    
    if (exid and prid):
        examproblems(examid=exid, problemid=prid).save()
    