def initialise(num_digits):

	num = ''

	for i in range(1, num_digits + 1):
		num += (str(i))
	return (int(num))

###########################################################

def largest_n_digit_num(num_digits):

	largest_num = ''
	for i in range(num_digits, 0, -1):
		largest_num += str(i)
	return (int(largest_num))

###########################################################

def has_same_digts(num):

	for i in range(len(num) - 1):
		if num[i] == num[i+1]:
			return False
	return True

###########################################################

def generate_order(num_digits):

	order = []
	initial_num = initialise(num_digits)
	largest_num = largest_n_digit_num(num_digits)
	for i in range(initial_num, largest_num):
		if(str(i) == ''.join(sorted(str(i))) and has_same_digts(str(i))):
			order.append(i)
	print(order)
	return order

###########################################################

def find_next_i(n, i, order):

	index = order.index(n)
	return (order[index + i % len(order)])

###########################################################

def find_prev_i(n, i, order):

	index = order.index(n)
	if (index - i < 0):
		return (order[index - i + len(order)])
	return (order[index - i])

###########################################################

def find_difference(num1, num2, order):

	index1 = order.index(num1)
	index2 = order.index(num2)
	return abs(index1 - index2) if index2 > index1 else (len(order) - abs(index1 - index2))

###########################################################

order = generate_order(5)
print(find_next_i(45678, 3 ,order))
print(find_prev_i(12345, 1, order))
print(find_difference(46789, 45678, order))