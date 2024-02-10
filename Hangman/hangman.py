import random

from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("HANGMAN")
    print(display_hangman(tries))
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed this letter")
            elif guess not in word:
                print(guess + " is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(guess + " in the word! Good job")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for i in indices:
                    word_as_list[i] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've already guessed this word")
            elif guess != word:
                print(guess + " is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not valid guess")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats!! You guessed the word!")
    else:
        print("You out of tries. The word was " + word)


def display_hangman(tries):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play again? Y/N ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
