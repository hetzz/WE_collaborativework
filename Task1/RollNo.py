def getMarks():
    f = open("marklist.txt", 'r')
    input_list = f.read().splitlines()
    marksheet = dict()
    return marksheet

def sortMarks() :
    for i in getMarks():
        rollno, marks = i.split()
        marks = int(marks)
        marksheet[rollno] = marks

    sorted_marksheet = (sorted(marksheet.items(), key = lambda marksheet: marksheet[1], reverse = True))
    return sorted_marksheet

def getRanks():
    sorted_marksheet = sortMarks()
    rank = 1
    ranks = []
    ranks += [(rank, sorted_marksheet[0][0], sorted_marksheet[0][1])]
    num_same_ranks = 0

    for i in range(1, len(sorted_marksheet)):
        if not(sorted_marksheet[i][1] == sorted_marksheet[i-1][1]):
            rank += 1
            num_same_ranks = 0
        else:
            num_same_ranks += 1
        ranks += [(rank, sorted_marksheet[i][0], sorted_marksheet[i][1])]


print(getRanks())
