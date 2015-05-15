# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def prime_fac(n):
    prime_factors = []
    i = 2
    
    # Only needs to go to sqrt of the number hence the iterator is squared
    while i*i <= n:

    	# Check to see if current iterator value is a factor 
        while (n % i) == 0:
            prime_factors.append(i)  # supposing you want multiple factors repeated
            n //= i
        i += 1

    # Adds the value as a factor since any num multiplied by one is itself
    if n > 1:
       prime_factors.append(n)
    return prime_factors