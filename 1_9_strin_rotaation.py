# question: assume you have a method isSubstring which check if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g. "waterbottle" is a rotation of "erbottlewat")

def isSubstring(s1, s2):
	return s1 in s2


def string_rotation(s1, s2):
	return isSubstring(s1, s2+s2)

assert string_rotation("waterbottle", "erbottlewat") == True