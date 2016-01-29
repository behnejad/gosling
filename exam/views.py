# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from exam.models import field, section, problem as prob, exam as examination, examproblems, useranswers
from user.models import User, group as Group, group_user_relation
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from rank import getExamScores
from django.db.models import Count, Max, Min, Avg


def index(request):
    return render(request, 'index.html')


def exam(request, eID):
    e = examination.objects.get(id=eID)
    if not e.isStart:
        return render(request, 'index.html')

    return render(request, 'exam.html', {'probs': examproblems.objects.filter(examid=eID),
                                         'exam': e, 'id': eID})


def answerProblem(request, mode=''):
    eID = request.POST['eID']
    pID = request.POST['problem']
    uID = request.session['userId']

    if mode == 'set':
        sel = int(request.POST['select'])
        uan = useranswers.objects.filter(examid=eID, problemid=pID, userid=uID)[:1]
        if uan.count():
            uan = uan[0]
            uan.answer = sel
            uan.save()

        else:
            useranswers(examid=examination.objects.get(id=eID), problemid=prob.objects.get(id=pID),
                        userid=User.objects.get(id=uID), answer=sel).save()

    if mode == 'del':
        useranswers.objects.filter(examid=eID, problemid=pID, userid=uID).delete()

    return HttpResponse('Y')


def group_exam_result(request, eID):
    res = getExamScores(eID)
    users_info = []
    mx, mn = -100, 100

    a = 0
    for i in res[0]:
        users_info.append({'name': res[0][i][2], 'correct': res[0][i][0], 'incorrect': res[0][i][1],
                           'darsad': float(3 * res[0][i][0] - res[0][i][1]) / float(3 * res[1])})

        if (users_info[-1]['darsad'] > mx):
            mx = users_info[-1]['darsad']

        if (users_info[-1]['darsad'] < mn):
            mn = users_info[-1]['darsad']

        a += users_info[-1]['darsad']

    return render(request, 'group_exam_result.html', {'avg_exam': float(a) / len(res[0]), 'min_exam': mn * 100,
                                                      'max_exam': mx * 100, 'users_info': users_info})


def exam_list(request):
    return render(request, 'index.html')


def admin(request, gId):
    g = Group.objects.get(id=gId)
    if request.session['userId'] == g.admin_id:
        print group_user_relation.objects.filter(group=gId, user=request.POST['user']).delete()

    return HttpResponseRedirect('/exam/group/%s' % gId)


def group(request, eID):
    g = Group.objects.get(id=eID)
    if request.method == 'POST':
        g.name = request.POST['name']
        g.save()

    use = False if request.session['userId'] == g.admin_id else True
    mems = group_user_relation.objects.filter(group=eID)
    exams = examination.objects.filter(groupid=eID)
    return render(request, 'group.html', {'group': g, 'mems': mems, 'user': use, 'exams': exams})


def makeExam(request):
    gr = request.POST.get('groupId')
    sd = request.POST.get('startDate')
    ed = request.POST.get('endDate')
    nm = request.POST.get('examName')

    if (gr and sd and ed and nm):
        a = examination(groupid=Group.objects.get(id=gr), startdate=datetime.strptime(sd, '%Y-%m-%d %I:%M %p'),
                    enddate=datetime.strptime(ed, '%Y-%m-%d %I:%M %p'), name=nm)
        a.save()
    else:
        return HttpResponseRedirect('/exam/group/%d' % gr)

    return render(request, 'pick_question.html', {'eID': a.id, 'gID': gr, 'probs': prob.objects.get_queryset()})


def selectQuestions(request):
    ex = examination.objects.get(id=request.POST['eID'])
    for i in request.POST.getlist('check'):
        examproblems(examid=ex, problemid=prob.objects.get(id=i)).save()

    return HttpResponseRedirect('/exam/group/%s' % request.POST['gID'])


def addToGroup(request):
    group_user_relation(user=User.objects.get(email=request.POST['mail']),
                        group=Group.objects.get(id=request.POST['gid'])).save()
    return HttpResponse('Yes')


def group_list(request):
    return render(request, 'groupList.html', {'list': Group.objects.get_queryset()})


def pick_question(request):
    questions_info = []
    question_info = {}

    question_info['info'] = "dsds"
    question_info['question'] = "صورت سوال"
    question_info['subject'] = "مهندسی نرم"
    question_info['id'] = 12
    for i in range(0, 10):
        questions_info.append(question_info)

    return render(request, 'pick_question.html', {'questions_info': questions_info})


def problem(request):
    p = prob.objects.filter(id=request.GET.get('id'))[0] if request.GET.get('id') else prob.objects.get_queryset()[:1][0]
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
                                                               'mess': 'الان تو گروهی  ؟'})

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
