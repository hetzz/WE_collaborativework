def generateSequence(number, iter, num_of_digits, sequence_list):
    if num_of_digits == 0:
        sequence_list.append(number)
        return
    for i in range((iter + 1), 10):
        generateSequence(number * 10 + i, i, num_of_digits - 1, sequence_list)
    return sequence_list


def getSequence(num_of_digits):
    number_list = []
    return generateSequence(0, 0, num_of_digits, number_list)


def initialize(num_of_digits):
    string_num = ""
    for i in range(1, num_of_digits + 1):
        string_num += str(i)
    return int(string_num)


def getNextNumber(number, sequence_list):
    index = sequence_list.index(number)
    if index+1 == len(sequence_list):
        return sequence_list[0]
    return sequence_list[index + 1]


def getPreviousNumber(number, sequence_list):
    index = sequence_list.index(number)
    length = len(sequence_list)
    if index == 0:
        return sequence_list[length - 1]
    return sequence_list[index - 1]

def differenceOfNumbers(first_number, second_number, sequence_list):
    first_num_index = sequence_list.index(first_number)
    second_num_index = sequence_list.index(second_number)
    return abs(second_num_index - first_num_index)

sequence_list = getSequence(3)
print(differenceOfNumbers(125, 236, sequence_list))
print(getNextNumber(789, sequence_list))
print(getPreviousNumber(789, sequence_list))