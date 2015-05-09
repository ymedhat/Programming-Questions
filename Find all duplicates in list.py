# Given a list of integers, return a list of all duplicates 

def find_dups(array_of_ints):
	numbers = list(len(array_of_ints))
	duplicates = []

	for num in array_of_ints:
		if numbers[num] = 1:
			duplicates.append(num)
		else:
			numbers[num] = 1

	# Solution can be extended to return only one of
	# each duplicate found by:
    # return list(set(duplicates))
	return duplicates