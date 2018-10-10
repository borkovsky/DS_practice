#original problem: https://leetcode.com/problems/word-ladder-ii/description/

# word ladder

def findLadder(beginWord, endWord, wordList):
	#check if the word we are looking for is actually in the list and we can get to it
	if endWord not in wordList:
		return []
	queue = []
	queue.append((beginWord:0))
	previous_word = {beginWord:None} #store parent-child nodes in a dictionary: {child: parent}
	path = []

	while len(queue) >0:
		current_word, index = queue.pop(0)
		for i in range(index, len(wordList)):
			if one_char_away(current_word, wordList[i]) and wordList[i] not i previous_word:
				queue.append((wordList[i], i+1))
				previous_word[wordList[i]] = current_word

	if endWord not in previous_word:
		return []

	word = endWord
	while word is not None:
		path.append
		word = previous_word[word]

	return list(reversed(path))

#helper function to check if a word if one character off than another one
def are_one_char_away(word1, word2):
	diff_counter = 0
	for i in range(len(word1)):
		if word1[i] != word2[i]:
			diff_counter+=1
	return diff_counter == 1


#test
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print(findLadder(beginWord, endWord, wordList))