import random
import string
from random_word import RandomWords
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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

def generate_image_hint(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n = 1,
            size = "1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print("Error generating image:", e)
        return None

def main():

    size = 4
    target = randword(size)
    attempts = 0
    max_attemps_before_hint = 5
    hint_given = False

    num = 0
    while(num == 0):
        
        input_word = input("Enter any "+str(size)+" letter word: \n")
        
        #input_word = input("Enter any \n")

        if(len(input_word) != size):
            continue

        match_count, char_set = posANDletter(input_word, target)
        mismatch_count = onlyletter(input_word, target, char_set)

        print(match_count, " piggy")
        print(mismatch_count, " oink")

        if(match_count == 0 and mismatch_count == 0):
            print("...snort..snort...")

        if(match_count == 4 and mismatch_count == 0):
            print("PIGGYYY!")
            num = 1
        
        attempts += 1
        
        if attempts >= max_attemps_before_hint and not hint_given:
            print("Looks like you could use some help. Generating an image hint...")
            image_url = generate_image_hint(target)
            if image_url:
                print(f"Here is your hint {image_url}")
            else:
                print("Failed to generate an image hint.")
            hint_given = True
        
        if attempts > 10:
            print("you lost. word was: " + target)
   
if __name__ == "__main__":
    main()