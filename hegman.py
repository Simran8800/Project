import string
from word import choose_word
from images import IMAGES

# End of helper code
# ----------------------------------
def ifvalid(user_input):
    if len(user_input)!=1:
        return False
    if not user_input.isalpha():
        return False
    return True


def is_word_guessed(secret_word, letters_guessed):
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True

    return False


def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    import string
    all_letters = string.ascii_lowercase
    letters_left=""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left+=letter
    return letters_left

def get_hint(secret_word,letters_guessed):
    import random
    letters_not_guessed=[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letters_not_guessed:
                letters_not_guessed.append(i)
    return random.choice(letters_not_guessed)

# remaining_lives=8
# totallives=remaning_lives=8
def hangman(secret_word):
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    # print ("")
    user_difficulty_choice=input("aap abi kitnea difficulty per yeh game khealna chahtea ho?\na)Easy\nb)tMedia\nc)Hard\n\nAapni choice a,b,ya c ki terms mai baatyea :-\n ")
    total_lives=remaning_lives=8
    image_selection=[0,1,2,3,4,5,6,7]

    if user_difficulty_choice not in ["a","b","c"]:
        print("Aapki choice invalid hai.\nGame easy mode mai start kar rahea hai")

# letters_guessed = []
# remaining_lives=8
# totallives=remaning_lives=8
# image_selection=[0,1,2,3,4,5,6,7]
# level=input("enter the level in which u want to play:\n""(a)for easy\n""(b)for medium\n""(c)for hard level:")
    else:
        if user_difficulty_choice=="b":
            total_lives=remaining_lives=6
            image_selection=[1,2,3,4,5,6,7]
        elif user_difficulty_choice=="c":
            total_lives=remaining_lives=4
            image_selection=[1,3,5,7]
        elif user_difficulty_choice=="a":
            total_lives=remaining_lives=8
            image_selection=[1,2,3,4,5,6,7]

    letters_guessed = []
    while remaining_lives>0:
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)
        guess =input("Please guess a letter: ")
        letter = guess.lower()
        if letter=="hint":
            print("your hint for the scret word is",get_hint(secret_word,letters_guessed))
# if (not ifvalid(letter)):
# continue
        elif (not ifvalid(letter)):
            print("invalid input")
            continue
        elif letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")
        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print(IMAGES[image_selection[total_lives-remaining_lives]])
# letters_guessed.append(letter)
# print(IMAGES[8,remaining_lives])
            remaining_lives-=1
            print("remaining_lives:"+str(remaining_lives))
            print ("")
            letters_guessed.append(letter)
            if is_word_guessed(secret_word,letters_guessed)==letters_guessed:
                print("* * congratulatins,you won!* *")
                print("")
    else:
        print("sorry,you ran out of guess.the word was"+str(secret_word)+".")
    # Load the list of words into the variable wordlist
    # So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)