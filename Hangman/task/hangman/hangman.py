# Write your code here
from random import choice
from string import ascii_lowercase

print("H A N G M A N\n")
words = ("python", "java", "kotlin", "javascript")
while True:
    while True:
        stop_word = input('Type "play" to play the game, "exit" to quit:')
        if stop_word == "play" or stop_word == "exit":
            break
        else:
            pass
    if stop_word == "play":
        pass
    else:
        break
    shadow_word = choice(words)
    word = "-" * len(shadow_word)
    letset = set()
    all_input_set = set()
    i = 0
    while i < 8:
        print(word)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter not in ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif letter in all_input_set:
            print("You already typed this letter")
        elif letter in shadow_word:
            word = ""
            letset.add(letter)
            for j in range(len(shadow_word)):
                if shadow_word[j] in letset:
                    word += shadow_word[j]
                else:
                    word += "-"
        else:
            print("No such letter in the word")
            i += 1
        if "-" not in word or i == 8:
            break
        print()
        all_input_set.add(letter)

    if "-" not in word:
        print(f"""{shadow_word}
        You guessed the word!
        You survived!\n""")
    else:
        print("You are hanged!\n")


