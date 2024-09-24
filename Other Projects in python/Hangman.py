import random

hangman = [
    '''
       +---+
           |
           |
           |
           |
           |
    =========''',  # 0 vidas perdidas
    '''
       +---+
       O   |
           |
           |
           |
           |
    =========''',  # 1 vida perdida
    '''
       +---+
       O   |
       |   |
           |
           |
           |
    =========''',  # 2 vidas perdidas
    '''
       +---+
       O   |
      /|   |
           |
           |
           |
    =========''',  # 3 vidas perdidas
    '''
       +---+
       O   |
      /|\  |
           |
           |
           |
    =========''',  # 4 vidas perdidas
    '''
       +---+
       O   |
      /|\  |
      /    |
           |
           |
    =========''',  # 5 vidas perdidas
    '''
       +---+
       O   |
      /|\  |
      / \  |
           |
           |
    =========''',  # 6 vidas perdidas (fim de jogo)
]

word_list = ["amor", "felicidade", "amizade", "coragem", "esperança", "sabedoria", "beleza", "natureza", "liberdade", "respeito"]
chosen_word = random.choice(word_list)
Len_CW = len(chosen_word)

placeholder = ""
words_lost = ""
life = 6

game_over = False

correct_letters = []

for position in range(Len_CW):
    placeholder += "_"

while not game_over:

    guess = input("Guess a letter!\n").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            
    if guess not in chosen_word:
        words_lost += guess
        life -= 1
        if life == 0:
            game_over = True
            print(f"You Lose! The word was: {chosen_word} ")

    print(display)

    if "_" not in display:
        game_over = True
        print("You won!")
    
    print(hangman[life])