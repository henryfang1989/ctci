# question: implement an algorithm to determine if a string has all unique characters. What if you cannot use additional structures?

def is_unique(s):
	ss = sorted(list(s))
	for i in xrange(len(ss)):
		if i == 0:
			continue
		elif ss[i] == ss[i-1]:
			return False
	return True

print is_unique("abc")
print is_unique("")
print is_unique("aa")
