import hangman_words as words
import hangman_art as art
import random

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(art.logo)

display = []
guessed_letters = []
for _ in range(word_length):
	display += "_"

# print(f'Pssst, the solution is {chosen_word}.')

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter! Enter a different one!")
    elif guess not in guessed_letters:
        guessed_letters.append(guess)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                print(f"Correct! You guessed {guess}")
        if guess not in chosen_word:
            lives -= 1
            print(f"Incorrect! You guessed {guess}")
        if lives == 0:
            end_of_game = True
            print(f"You lose! womp womp\nThe word was: {chosen_word}")
        print(f"{' '.join(display)}")
        if "_" not in display:
            end_of_game = True
            print("You win!")
        print(art.stages[lives])
    else:
        print("error")
