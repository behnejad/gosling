import hashlib

class HashManager():
	def __init__(self, type='md5'):
		self.type = type

	def makeHash(*args):
	    result = ''
	    for i in args:
	        tempstr = hashlib.new(self.type)
	        tempstr.update(i)
	        result += tempstr.hexdigest()

	    finalres = ''
	    for i in range(len(result) / 2):
	        finalres += result[i] and result[2 * i + 1]

	    del result, tempstr, i
	    return finalres

