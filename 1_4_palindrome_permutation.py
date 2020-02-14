# question: Given a string, write a fuction to check if it it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 

# Example:
# Input: Tact Coa
# Output: True (permutations: "taco cat" "atco cta", etc)

def palindrome_permutation(s):
	hashmap = {}
	odd = 0
	for c in s:
		if c == " ":
			continue
		if c not in hashmap:
			hashmap[c] = 1
		else:
			hashmap[c] += 1
		
		# run one passs
		if hashmap[c] % 2 == 1:
			odd += 1
		else:
			odd -= 1
			
	return odd < 2

assert palindrome_permutation("aa") == True
assert palindrome_permutation("ab") == False
assert palindrome_permutation("") == True
assert palindrome_permutation("aabaa") == True
assert palindrome_permutation("tact coa") == True

# time : O(n)
# space: O(n)
# n = length of string
