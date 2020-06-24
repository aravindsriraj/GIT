import random

print("H A N G M A N")
play_or_exit = input('Type "play" to play the game, "exit" to quit: > ')
while play_or_exit=='play':

    words = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = random.choice(words)
    guessed_letters = list('-' * len(chosen_word))
    user_letters = set()
    has_won = False

    tries = 8
    #game loop
    while tries > 0: 
        print()
        for x in guessed_letters:
            print(x, end='')
        
        letter = input("\nInput a letter: ")
        if len(letter) > 1:
            print("You should input a single letter")
            continue
        
        if letter.isupper() or not letter.isalpha():
            print("It is not an ASCII lowercase letter")
            continue
            
        if letter in user_letters:
            print("You already typed this letter")
            continue
        
        user_letters.add(letter)
        
        if letter not in chosen_word:
            print("No such letter in the word")
            tries -= 1
            continue 
        else:
            for j in range(0, len(chosen_word)):
                if chosen_word[j] == letter:
                    guessed_letters[j] = letter
                    
            if '-' not in guessed_letters:
                has_won = True
                break   
        
    if has_won:
        print(f"You guessed the word {chosen_word}!")
        print("You survived!")
    else:
        print("You are hanged!")
    print()
    play_or_exit = input('Type "play" to play the game, "exit" to quit: > ')