# write a method to replace all spaces in a string with "%20". You may assume that the string has sufficient spaces at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: if implementing in java, pleae use a character array so that you can perform this operation in place.)

# Input: "Mr John Smith.    ", 13
# Output: "Mr%20John%20Smith"


def urlify(strlist, length):
	replace = "%20"
	tail = length-1
	
	i = len(strlist)-1
	while tail >= 0:
		if strlist[tail] != " ":
			strlist[i] = strlist[tail]
			i -= 1
			tail -= 1
		else:
			tail -= 1
			for j in xrange(len(replace)):
				strlist[i] = replace[j]
				i -= 1
	return strlist
		
				
	
str = "Mr John Smith    "
print urlify(list(str), 13)
