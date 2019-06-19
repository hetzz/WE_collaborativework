def gen_word_list(n):
    file = open("sowpods.txt", 'r')
    content = file.readlines()
    words = []
    for word in content:
        if len(word) == n + 1:
            words.append(word[:-1])   
    return words

def update_list(given_word , words, similar_num):
    remove = []
    for i in words :
        if (len(set(i).intersection(set(given_word)))) != similar_num :
            remove.append(i)
    remove.append(given_word)
    return [word for word in words if word not in remove]

def play_game(n):
    words = gen_word_list(n)
    GAME = True
    while GAME :
        print("I am guessing a word from ",len(words)," words")
        if(len(words) == 0):
            print("I can't guess from any more words :(")
            print("You've cheated :(")
            break
        print("How many are similar in this word : ",words[0])
        tmp = words[0]
        similar_num = input()
        if(similar_num == "WIN"):
            print("YAYAYAYA")
            con = input("\n\nDo you want to continue(y/n)?")
            if con == 'y':
                restart()
            elif con == 'n' :
                break
        words = update_list(tmp, words, int(similar_num))

def restart():
    n = int(input("Enter the length of the word you thought"))
    play_game(n)

restart()