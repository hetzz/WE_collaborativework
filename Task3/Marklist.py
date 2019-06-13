def isgreater(student1 , student2):
    greaterThanCheck = sum(list(1 for i in range(3) if int(student1[i]) > int(student2[i]) ))
    return greaterThanCheck == 3

def removeTransitive(greaterThanPairs) :
    transitive_pairs = []
    for pair1 in greaterThanPairs:
        check_var = pair1[1]
        for pair2 in greaterThanPairs :
            if pair1 != pair2:
                if pair2[0] == check_var:
                    s = str(pair1[0]) + str(pair2[1])
                    transitive_pairs.append(s)
    return [pairs for pairs in greaterThanPairs if pairs not in transitive_pairs]


def generateGreaterPairs(marksList):
    greaterThanPairs = []
    for student1 in (marksList) :
            for student2 in (marksList):
                if(isgreater(student1[1:],student2[1:])):
                    greaterThanPairs .append(str(student1[0]) + str(student2[0]))
    
    return greaterThanPairs

def compareFunction() :
    
    with open("Marks.txt", "r") as marksFile :
        marksList = list(marksFile.read().strip().split("\n"))
        marksList = [list(student.split(" "))for student in marksList]
        
        greaterThanPairs =  generateGreaterPairs(marksList)
        return removeTransitive(greaterThanPairs)

print(compareFunction())
