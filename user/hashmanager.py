import hashlib


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
