import random
import string
from random_word import RandomWords

'''
piggy game

'''
def posANDletter(word, target):
    
    count = 0
    char_set = set()

    for char1, char2, in zip(word, target):
        if char1 == char2: 
            char_set.add(char1)
            count += 1
    
    return count, char_set

def onlyletter(word, target, char_set):
    
    target_set = set(target)
    count = 0

    for i in range(len(word)):
        if word[i] in target_set and word[i] != target[i]:
            if word[i] not in char_set:
                count += 1

    return count

def randword(size):
    #r_string = "".join(random.choices(string.ascii_lowercase, k=4))
    r = RandomWords()
    word = ""
    while(len(word) != size):
        word = r.get_random_word()

    return word

def main():
    
    size = 4
    target = randword(size)

    num = 0
    while(num == 0):
    
        input_word = input("Enter any", size, " letter word: \n")

        if(len(input_word) != size):
            continue

        match_count, char_set = posANDletter(input_word, target)
        mismatch_count = onlyletter(input_word, target, char_set)

        print(match_count, " pig")
        print(mismatch_count, " oink")

        if(match_count and mismatch_count == 0):
            print("...snort..snort...")

        if(match_count == 4 and mismatch_count == 0):
            print("PIGGYYY!")
            num = 1

if __name__ == "__main__":
    main()