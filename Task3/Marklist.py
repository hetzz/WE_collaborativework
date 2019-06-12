def isgreater(student1 , student2):

    greaterThanCheck = sum(list(1 for i in range(3) if int(student1[i]) > int(student2[i]) ))
    return greaterThanCheck == 3

# def checkTransitive(greaterThanPairs) :
#     transitive = []
#     for i in greaterThanPairs :

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
        
        return generateGreaterPairs(marksList)

print(compareFunction())
