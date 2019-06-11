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

def generate_order(num_digits):

	order = []
	initial_num = initialise(num_digits)
	largest_num = largest_n_digit_num(num_digits)
	for i in range(initial_num, largest_num):
		if(str(i) == ''.join(sorted(str(i)))):
			order.append(i)
	return order

###########################################################

def find_next_i(n, i, order):
	ind = order.index(n)
	return (order[ind + i])

###########################################################

def find_prev_i(n, i, order):
	ind = order.index(n)
	return (order[ind - i])

###########################################################

order = generate_order(5)
print(find_next_i(45678, 3 ,order))