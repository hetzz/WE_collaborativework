
def get_words(file_name):
    with open(file_name) as f:
         return [x.strip() for x in f]

def valid_word(word):
    if word in get_words("../sowpods.txt"):
        return word

def changing_letter(word1: str, word2: str):
    if len(word1) != len(word2):
        return 
    else: 
        return min_no_of_letters(word1, word2)

def min_no_of_letters(word1, word2):
    word = word1
    for i in range(len(word2)):
        if word[i] != word2[i]:
            word = word.replace(word[i], word2[i])
            valid_word(word)
            print(word)
    return word

print(changing_letter("salt", "gold"))