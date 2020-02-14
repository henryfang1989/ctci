# question: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

# Example:
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def one_away(s1, s2):
	if len(s1) == len(s2):
		return check_replace(s1, s2)
	if len(s1) > len(s2):
		return check_insert(s2, s1)
	else:
		return check_insert(s1, s2)

def check_replace(s1, s2):
	if len(s1) == len(s2) == 0:
		return False
	diff = 0
	for i in xrange(len(s1)):
		if s1[i] != s2[i]:
			diff += 1
			if diff > 1:
				return False
	return True
# time: O(n)
# space: O(1)

def check_insert(s1, s2):
	if len(s1) + 1 != len(s2):
		return False
	diff = i = j = 0
	while i < len(s1):
		if s1[i] == s2[j]:
			i += 1
			j += 1
		else:
			j += 1
			diff += 1
			if diff > 1:
				return False
	return True
# time: O(n)
# space: O(1)
# n = length of string


assert one_away("pale", "ple") == True
assert one_away("pales", "pale") == True
assert one_away("pale", "bale") == True
assert one_away("pale", "bae") == False
assert one_away("", "") == False
assert one_away("", "a") == True

