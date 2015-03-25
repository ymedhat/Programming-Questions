def get_nth_node(pointer, node):
	itr = pointer
	for i in range(node):
		itr.next_node()
	while itr != None:
		itr.next_node()
		pointer.next_node()
	return pointer
