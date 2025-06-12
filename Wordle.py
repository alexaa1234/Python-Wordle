import random

secret_word = ['Cells', 'Genes', 'Nerve', 'Algae']
secret_word = [word.lower() for word in secret_word]
chosen_word = random.choice(secret_word)

word_length = len(chosen_word)
guessed_words = []
lives = 5

while lives > 0:
    guess = input("Guess the 5 letter word: ").lower() 

    if len(guess) !=5:
        print("Please input a 5 letter word.")
        continue

    if not guess.isalpha():
        print("Please only put letters from the alphabet")
        continue

    if guess in guessed_words:
        print("You've already guessed that word, try another one")
        continue

    guessed_words.append(guess)

    if guess == chosen_word:
        print ("You got the word correct, congratulations! \n")
        break
    
    feedback = ""
    correct_letter = 0
    for i in range(len(chosen_word)):
        if  chosen_word[i] == guess[i]:
            correct_letter += 1
            feedback += f"[{guess[i]}]"
           
        
        elif  guess[i] in chosen_word:
            correct_letter += 1
            feedback += f"({guess[i]})"
        
        else:
            feedback += f" {guess[i]} "

    print(feedback)
          


    lives -=1
    print(f"You have {lives} lives left.\n")

if lives == 0:
    print(f"You have run out of lives. The word is {chosen_word}.\n")


            




    
    