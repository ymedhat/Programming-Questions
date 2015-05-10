#Write a method to generate the nth Fibonacci number

def fib_num(nth_num):
	if nth_num is 0:
		return 0

	elif nth_num is 1:
		return 1

	# If the nth number is greater than one,
	# we recursively call the function on the
	# previous values as the Fibonacci sequence
	# requires
	else:
		return fib_num(nth_num-1)+fib_num(nth_num-2)