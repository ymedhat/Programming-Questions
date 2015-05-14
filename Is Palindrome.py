#Find the largest palindrome made from the product of two n-digit numbers.
def palin(n):
	palin = []
	lwr_bnd = 10**(n-1)
	uppr_bnd = 10**n
    # Use two for-loops of order n squared to multiple all
    # combinations of n-digit number
	for i in range(lwr_bnd,uppr_bnd):
		for j in range(lwr_bnd,uppr_bnd):
			num = i*j
            
            # Using pythonic syntax, this checks if a string
            # is equal to its reversed version
			if str(num) == str(num)[::-1]:
				palin.append(num)
	palin.sort()
    # Returns a set to remove any duplicates within the created array
	return set(palin)