def find_transitive(list):
    transitive_pairs = []
    for i in list:
        temp = i[1]
        for j in list :
            if i != j:
                if j[0] == temp:
                    s = str(i[0]) + str(j[1])
                    transitive_pairs.append(s)
    return transitive_pairs

print (find_transitive(["ab","bc","da"]))






