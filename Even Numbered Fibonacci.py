# By considering the terms in the Fibonacci sequence 
# whose values do not exceed large values(i.e. four million),
# find the sum of the even-valued terms

def fib(n):
	count = 2
	num = 3
	num_array = [1,2]
	
	if n is 0:
		return 0

	elif n is 1:
		return 1

	else:
		while num < n:

			if num%2 is 0:
				count += num

			# Shift the Fibonacci numbers
			# to only use an array of size 2
			# due to large numbers	
			num_array[0] = num_array[1]
			num_array[1] = num

			# Calculate next Fibonacci Number
			num = sum(num_array)

	return count