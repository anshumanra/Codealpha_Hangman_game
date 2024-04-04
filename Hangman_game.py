import random

def choose_word(level):
    easy_words = ['apple', 'banana', 'orange', 'chair', 'table', 'jump', 'tree', 'house', 'smile', 'happy', 'color', 'music', 'friend', 'water', 'cloud', 'watch', 'learn', 'dance', 'story', 'world', 'flower', 'summer', 'winter', 'pencil', 'picnic', 'party', 'laugh', 'dream', 'light', 'beach', 'build', 'swing', 'slide', 'candy', 'puppy', 'kitten', 'train', 'truck', 'bike', 'plane', 'sleep', 'star', 'moon', 'love', 'sing', 'read', 'draw', 'paint', 'cook', 'bake', 'swim', 'play', 'game']
    medium_words = ['python', 'window', 'rainbow', 'blanket', 'picture', 'present', 'bicycle', 'dolphin', 'pumpkin', 'spider', 'cowboy', 'secret', 'rocket', 'island', 'forest', 'garden', 'button', 'pocket', 'shadow', 'puzzle', 'bubble', 'robot', 'pillow', 'turtle', 'dragon', 'castle', 'pirate', 'parrot', 'monkey', 'orange', 'purple']
    hard_words = ['butterfly', 'elephant', 'dinosaur', 'volcano', 'umbrella', 'alligator', 'computer', 'airplane', 'surprise', 'vacation', 'lemonade', 'sunglasses', 'basketball', 'adventure', 'celebrate', 'remember', 'whisper', 'imagine', 'treasure', 'invisible', 'question', 'tomorrow', 'yesterday', 'important', 'different', 'beautiful', 'wonderful', 'amazing', 'delicious', 'impossible']

    if level == 'easy':
        return random.choice(easy_words)
    elif level == 'medium':
        return random.choice(medium_words)
    elif level == 'hard':
        return random.choice(hard_words)
    else:
        print("Invalid level selection.")
        return None

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    max_attempts = 7
    guessed_letters = []
    level = input("Select a level (easy, medium, hard): ").lower()
    word = choose_word(level)
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess not in word:
            attempts += 1
            print(f"Incorrect! You have {max_attempts - attempts} attempts left.")
            if attempts >= max_attempts:
                print("Game over! The word was:", word)
                break
        else:
            print("Correct!")

        display = display_word(word, guessed_letters)
        print(display)

        if '_' not in display:
            print("Congratulations! You guessed the word:", word)
            break

if __name__ == "__main__":
    hangman()


#CODE BY ANSHUMAN