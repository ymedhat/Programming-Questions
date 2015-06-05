# Given n integer, using its digits find the next largest value
# For example, given n = 123, return 132
def find_lrgr(n):
	string_num = str(n)
	i = -1
	left = string_num[i-1]
	right = string_num[i]

	# Find where right number is greater than left
	while (abs(i)-1) <= len(string_num):
		i -= 1
		if right > left:
			tmp = i
			i = len(string_num)+2
		else:
			right = string_num[i]
			left = string_num[i-1]
	index = len(string_num) + tmp
	minim = string_num[index]
	
	diff = int(string_num[index+1]) - int(left)

	# Find number to the right of the indexed int
	# that holds the smallest difference
	for num in range(index+1, len(string_num)):
		if int(string_num[num]) > int(left):
			if (int(string_num[num]) - int(left)) <= diff:
				minim = string_num[num]
				tmp = num

	# Concatenate the string to sort all numbers after indexed value
	# to create the next larger value
	right_side = string_num[index:tmp] + string_num[tmp+1:]
	right_side = [int(i) for i in right_side]
	right_side.sort()
	right_side = ''.join(map(str, right_side))
	new_num = string_num[0:index] + minim + str(right_side)
	return new_num 