# question: Implement a method to perform basic string compression using the counts of repeated charcaters. For example, the string "aabcccccaa" would become "a2b1c5a3". If the "compressed" string would not become smaller tan the orginal string, you method shpould return the origin string. You can assume the string has only uppercase and lowcase letters

def string_compression(s):
	if not s:
		return s

	# check if compressed string is shorter than orignal string
	compressed_len = 0
	i = 0
	while i < len(s):
		current = s[i]
		cnt = 0
		while i < len(s) and s[i] == current:
			cnt += 1
			i += 1
		compressed_len += 1 + len(str(cnt))
	if compressed_len >= len(s):
		return s

	i = 0
	res = ""
	while i < len(s):
		# set the state
		current = s[i]
		count = 0
		# find all occurances
		while i < len(s) and s[i] == current:
			count += 1
			i += 1
		# be careful here: because it is very inefficiency when it is always a single character. A better way to prevent it is just check if compressed string is shorter than original string before doing the real work.
		res += current + str(count)

	return res
# time: O(n)

assert string_compression("ab") == "ab"

assert string_compression("aaaab") == "a4b1"

assert string_compression("Aaabb") == "Aaabb"

assert string_compression("aabcccccaaa") == "a2b1c5a3"
