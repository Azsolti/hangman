from art import *
import time
import random
from colorama import Fore, Back, Style

with open('message.txt', 'r') as f:
    lines = f.readlines()
    words = []
    for n in lines:
        x = n.split('\n')
        for c in x:
            xs = c.split('|')
            for n in xs:
                if n == "":
                    pass
                else:
                    words.append(n.strip())


def hangman(word):

    while True:

        try:
            difficulty = int(input("Please select a difficulty(Easy - 1, Medium - 2, Hard - 3):"))
            
            if difficulty == 1:
                print('You have chosen Easy, you have 7 lives')
                lives_left = 7
                break

            elif difficulty == 2:
                print('You have chosen Medium, you have 5 lives')
                lives_left = 5
                break

            elif difficulty == 3:
                print('You have chosen Hard, you have 3 lives')
                lives_left = 3
                break

            else:
                print("Chose a valid number")
 
        except ValueError:
            print("Wrong input")
            pass

    startgame = input("Press any key to continue..")
    print(Fore.GREEN + "The game is now starting" + Style.RESET_ALL)
    time.sleep(1)

    word_count = len(word)
    characters_found = []
    wrong_characters = []

    while True:

        if len(characters_found) == word_count:
            print(f'\n')
            text = text2art("Congratulations! You found the word!", font="small")
            text_2 = text2art(word, font='small')
            print(Fore.GREEN + text + Fore.WHITE + text_2 + Style.RESET_ALL)
            
            break

        player_guess = input(f"\nGuess a letter:")

        if player_guess == "quit":
            print("Quitting the game. Good Bye")
            break
        
        elif player_guess.isalpha() and len(player_guess) == 1 or player_guess.isspace() and len(player_guess) == 1:

            if player_guess.lower() in word.lower():

                if player_guess in characters_found:
                    print(Fore.YELLOW)
                    tprint("You already have this letter, continuing..", font="tiny")
                    print(Style.RESET_ALL)
                    pass
            
                else:
                    for n in range(word.lower().count(player_guess.lower())):
                        characters_found.append(player_guess.lower())

                    print(Fore.GREEN )
                    tprint("You found a letter!" , font="tiny")
                    print(Style.RESET_ALL)

                    if len(set(wrong_characters)) >= 1:
                        print(f' Your wrong guesses: {set(wrong_characters)}')
                    
                    for char in word:

                        if char.lower() in characters_found:
                            print(Back.WHITE + char, end=' ' + Style.RESET_ALL)

                        else:
                            print(Back.WHITE + " _ ", end='' + Style.RESET_ALL)
                            
            else:
                print(Fore.RED + "No letters found :/")
                
                if player_guess in wrong_characters:
                    print(Fore.YELLOW)
                    tprint(f"Letter already guessed.. Your wrong guesses: {set(wrong_characters)}", font="tiny")
                    tprint(f'You   have   {lives_left}   lives   left', font="tiny")
                    print(Style.RESET_ALL)
                    
                    for char in word:

                        if char.lower() in characters_found:
                            print(Back.WHITE + char, end=' ' + Style.RESET_ALL)

                        else:
                            print(Back.WHITE + " _ ", end='' + Style.RESET_ALL)
                
                else:

                    lives_left -= 1
                    tprint(f'You   have   {lives_left}   lives  left', font="tiny")
                    print(Style.RESET_ALL)
                    wrong_characters.append(player_guess)
                    print(f' Your wrong guesses: {set(wrong_characters)}')
                    
                    for char in word:

                        if char.lower() in characters_found:
                            print(Back.WHITE + char, end=' ' + Style.RESET_ALL)

                        else:
                            print(Back.WHITE + " _ ", end='' + Style.RESET_ALL)
            
            if lives_left == 0:
                print(Fore.RED)
                print(f'The game is over. The word was : {word}. Better luck next time!')
                print(Style.RESET_ALL)
                break

        else:
            print("Invalid input, you can only use single letters")


words_index = random.randint(0,len(words)-1)
hangman(words[words_index])









    



