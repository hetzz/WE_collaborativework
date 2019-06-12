def initialise(num_digits):

	num = ''

	for i in range(1, num_digits + 1):
		num += str(i)
	return (int(num))

######################################################################################################################

def largest_n_digit_num(num_digits):

	largest_num = ''
	start_digit = 9
	
	for i in range(num_digits, 0, -1):
		largest_num += str(9)
		start_digit -= 1
	return (int(largest_num))

######################################################################################################################

def has_unique_digits(num):

	return (len(set(num)) == len(num))

######################################################################################################################

def isAscending(num):

	return (num == ''.join(sorted(num)))

######################################################################################################################

def generate_order(num_digits):

	initial_num = initialise(num_digits)
	largest_num = largest_n_digit_num(num_digits)
	
	return [i for i in range(initial_num, largest_num) if has_unique_digits(str(i)) and isAscending(str(i))]

######################################################################################################################

def find_next_i(n, i, order):

	index = order.index(n)
	return (order[index + i % len(order)]) if index != -1 else ("Not a valid reading")

######################################################################################################################

def find_prev_i(n, i, order):

	index = order.index(n)
	if (index - i < 0):
		return (order[index - i + len(order)])
	return (order[index - i]) if index != -1 else ("Not a valid reading")

######################################################################################################################

def find_difference(num1, num2, order):

	index1 = order.index(num1)
	index2 = order.index(num2)
	return abs(index1 - index2) if index2 > index1 else (len(order) - abs(index1 - index2))

######################################################################################################################

order = generate_order(5)
# print(find_next_i(45678, 3 ,order))
# print(find_prev_i(12345, 1, order))
# print(find_difference(46789, 45678, order))