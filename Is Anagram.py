#Write a method to decide if two strings are anagrams or not

from collections import defaultdict

def is_anagram(word_one, word_two):

	size_one = len(word_one)
	size_two = len(word_two)

	# First check if both strings hold same size
	if size_one != size_two:
		return False

 	dict_chars = defaultdict(int)

 	# Use dictionary to store both characters and how many
 	# times they appear in one dictionary
 	for chars in word_one:
 		dict_chars[chars] += 1

	for chars in word_two:
 		dict_chars[chars] += 1
 	
 	# Each character has to be divisible by two since 
 	# characters for both words are stored in the same 
 	# dictionary
 	for key in dict_chars:
 		if (dict_chars[key] % 2) != 0:
 			return False

 	return True
