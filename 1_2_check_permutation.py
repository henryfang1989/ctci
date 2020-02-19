# given two strings, write a method to decide if one is a permutation of the other.

def check_permutation_1(s1, s2):
	return sorted(s1) == sorted(s2)

def check_permutation_2(s1, s2):
	from collections import Counter
	return Counter(s1) == Counter(s2)

assert check_permutation_1("abc", "bca") == True
assert check_permutation_1("", "") == True
assert check_permutation_1("", "a") == False
assert check_permutation_1("aa", "ab") == False

assert check_permutation_2("abc", "bca") == True
assert check_permutation_2("", "") == True
assert check_permutation_2("", "a") == False
assert check_permutation_2("aa", "ab") == False