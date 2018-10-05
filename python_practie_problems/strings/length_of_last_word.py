def lengthOfLastWord(s):
	#split the input string into a list of words
	s_list = s.split()
	if len(s_list) < 1:
		return 0	#no last word
	else:
		return len(s_list[-1])

