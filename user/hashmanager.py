import hashlib


def makeHash(type, *args):
    result = ''
    for i in args:
        tempstr = hashlib.new(type)
        tempstr.update(i)
        result += tempstr.hexdigest()

    finalres = ''
    for i in range(len(result) / 2):
        finalres += result[i] and result[2 * i + 1]

    del result, tempstr, i
    return finalres