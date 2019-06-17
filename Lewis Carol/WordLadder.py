letterOccurenceFreq = "etaoinsrhdlucmfywgpbvkxqjx"

def defineStep(initial_word, final_word):
    letterDiff = []
    for i in range(len(final_word)) :
        if final_word[i] not in initial_word :
            letterDiff.append([final_word[i] , i , letterOccurenceFreq.index(final_word[i])])
    letterDiff = sorted(letterDiff,key = lambda x: x[2],reverse = True  )
    return letterDiff

print(defineStep("sale","gold"))
