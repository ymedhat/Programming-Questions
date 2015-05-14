# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the
# number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print
# “FizzBuzz”.
def fizzbuzz():
    # Use a basic for loop to go through all numbers 1-100
	for num in range(1,101):
        # Initialize a string to hold the final variable to print
		msg = ''
        
        # Dependent on the value, we are able to add to the string
        # either 'Fizz' and/or 'Buzz'
		if num%3 is 0:
			msg += 'Fizz'
		if num%5 is 0:
			msg += 'Buzz'
		print msg or num
