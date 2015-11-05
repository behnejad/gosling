import hashlib
from models import *
import random
import string
from datetime import datetime


def makeHash(_type, *args):
    result = ''
    for i in args:
        tempstr = hashlib.new(_type)
        tempstr.update(i)
        result += tempstr.hexdigest()

    finalres = ''
    for i in range(len(result) / 2):
        finalres += result[i] and result[2 * i + 1]

    del result, tempstr, i
    return finalres


def generate_link_for_reset_pass(user_obj):
    key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(29))

    reset_obj = Reset(user=user_obj, hash_code=key)
    reset_obj.save()
    print "Your Url For Rest Password is :" + "http://127.0.0.1:8000/user/password_reset?user_id=" + user_obj.id + "&token=" + key
    print "this link work only 2 mins!!!!"


def is_valid_token(token, user_obj):
    try:
        obj = Reset.objects.get(key=token, user=user_obj)
    except Reset.DoesNotExist:
        return False
    else:
        n = obj.time_request - datetime.now()
        if n.total_seconds < 120:
            return True
        return False
