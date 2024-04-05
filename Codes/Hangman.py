import random
def select_word():
    words=["black","pink","blue","green","red","orange","purple","yellow"]
    return random.choice(words)
def display_word(word, guessed_letters):
    display=""
    for letter in word:
        if letter in guessed_letters:
            display=display+letter
        else:
            display=display+"\t_"
        return display
def hangman():
    word=select_word()
    guessed_letters=[]
    no_of_attempts_left=8
    print("Hi, this is Hangman")
    print("Try guessing a word. The words are colors.")
    while no_of_attempts_left>0:
        print("\n Word:",display_word(word, guessed_letters))
        guess=input("Enter a letter:").lower()
        if guess in guessed_letters:
            print("Yay! You guessed it right.")
        elif guess in word:
            print("Right guess!!")
            guessed_letters.append(guess)
        if set(word) == set(guessed_letters):
            print("Hurray!! You have guessed the word:",word)
            break
        else:
            print("Try again.")
            no_of_attempts_left=no_of_attempts_left-1
            print("Number of attempts left:",no_of_attempts_left)
        if no_of_attempts_left==0:
            print("\nGAme is Over! The word was:",word)
            break
if __name__=="__main__":
    hangman()

