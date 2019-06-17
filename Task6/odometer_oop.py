class odometer:
	def __init__(self, n):
		self.n = n

	def initialise(self):

		num = ''

		for i in range(1, self.n + 1):
			num += str(i)
		return int(num)

	def largest_n_digit_num(self):

		largest_num = ''
		start_digit = 9

		for i in range(self.n, 0, -1):
			largest_num += str(9)
			start_digit -= 1
		return int(largest_num)

	def has_unique_digits(self, num):

		return len(set(num)) == len(num)

	def isAscending(self, num):

		return num == ''.join(sorted(num))

	def generate_readings(self):

		initial_num = self.initialise()
		largest_num = self.largest_n_digit_num()
		
		return [i for i in range(initial_num, largest_num) if self.has_unique_digits(str(i)) and self.isAscending(str(i))]

	def find_next_i(self, reading, i, readings):

		index = readings.index(reading)
		return readings[index + i % len(readings)] if index != -1 else "Not a valid reading"

	def find_prev_i(self, reading, i, readings):

		index = readings.index(reading)
		if (index - i < 0):
			return (readings[index - i + len(readings)])
		return readings[index - i] if index != -1 else "Not a valid reading"

	def find_difference(self, reading1, reading2, readings):

		index1 = readings.index(reading1)
		index2 = readings.index(reading2)
		return index2 - index1 if index2 > index1 else len(readings) - (index1 - index2)

odo1 = odometer(5)
readings = odo1.generate_readings()
print(odo1.find_next_i(35689, 3, readings))
print(odo1.find_difference(12569, 13467, readings))