from user.models import *
import random
import string
from datetime import datetime


def generate_link_for_reset_pass(user_obj):
    key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(29))

    reset_obj = Reset(hash_code=key, time_request=datetime.now(), user_id=user_obj.id)
    reset_obj.save()
    print "Your Url For Rest Password is :" + "/password_reset?user_id=" + str(user_obj.id) + "&token=" + key
    print "this link work only 2 mins!!!!"


def is_valid_token(token, user_obj):
    try:
        obj = Reset.objects.get(hash_code=token, user_id=user_obj.id)
    except Reset.DoesNotExist:
        return False
    else:
        if token_is_expired(obj.time_request):
            return False
        return True


def token_is_expired(time_create):
    return (datetime.now() - time_create).total_seconds() > 600
