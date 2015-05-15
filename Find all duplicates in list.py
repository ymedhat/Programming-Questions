# Given a list of integers, return a list of all duplicates 
def find_dups(int_array):
	# Checks base case of empty list
	if not int_array:
		return None

	# Sort the array to group all duplicates
	int_array.sort()

	# Create an array of size two to shift 
	# integers into
	dups = [0]*2

	# Create array to store duplicate values
	dup=[]

	# Copy first two integers into array
	dups[0:2] = int_array[0:2]

	# Iterate through array of integers,
	# and check for any duplicates
	for num in range(0,len(int_array)-1):
		if dups[0] == dups[1]:
			dup.append(dups[0])

		# Shift the next integer
		dups[0:2] = int_array[num:num+2]

	# If there are duplicates, then return sorted list
	# with only one duplicate for each integer using a set
	if len(dup)>1:
		return list(set(dup.sort()))
	
	elif len(dup)==1:
		return dup
	
	else:
		return None



import pdb
pdb.set_trace()
find_dups([1,1])