
from exam.models import field, section, problem as prob, exam as examination, examproblems, useranswers



def getExamScores(exami, perproblem=False):
    anscount = examproblems.objects.filter(examid=exami).count()
    userStatus = {} #[{'hooman': [0, 0], 'omid': []}, 0]
    
    for u in useranswers.objects.filter(examid=exami):
        if (perproblem):
            k = u.problemid.id
        else:
            k = u.userid.id
        if (k in userStatus):
            if (u.answer == u.problemid.correctanswer):
                userStatus[k][0] += 1
            else:
                userStatus[k][1] += 1
        else:
            m = [0,0,u.userid.person]
            if (u.answer == u.problemid.correctanswer):
                m[0] += 1
            else:
                m[1] += 1
            userStatus[k] = m
    return userStatus, anscount


def getUserScores(useri):
    userStatus = {} #[{'hooman': [0, 0], 'omid': []}, 0]
    
    for u in useranswers.objects.filter(userid=useri):
        anscount = examproblems.objects.filter(examid=u.examid).count()
        k = u.examid.name
        if (k in userStatus):
            if (u.answer == u.problemid.correctanswer):
                userStatus[k][0] += 1
            else:
                userStatus[k][1] += 1
        else:
            m = [0,0]
            if (u.answer == u.problemid.correctanswer):
                m[0] += 1
            else:
                m[1] += 1
            userStatus[k] = m
    return userStatus, anscount