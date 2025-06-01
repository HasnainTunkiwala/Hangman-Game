import random

# Word list (you can expand this or load from a file)
word_list = ['python', 'developer', 'hangman', 'challenge', 'programming']

# Choose a random word
word = random.choice(word_list)
word_letters = set(word)
guessed_letters = set()
lives = 6

print("🎯 Welcome to Hangman!")

while len(word_letters) > 0 and lives > 0:
    print("\nYou have", lives, "lives left.")
    # Show current word state
    current_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: ", ' '.join(current_word))

    # Get user input
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("✅ Good guess!")
    else:
        lives -= 1
        print("❌ Wrong guess!")

# End of game
if lives == 0:
    print("\n💀 Game over! The word was:", word)
else:
    print("\n🎉 You guessed the word:", word)


    
    
