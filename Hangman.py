import random
def hangman():

          stages = ['''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
          =========
          ''', '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
          =========
          ''', '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
          =========
          ''', '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
          =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
          =========
          ''', '''
            +---+
            |   |
            O   |
                |
                |
                |
          =========
          ''', '''
            +---+
            |   |
                |
                |
                |
                |
          =========
          ''']
          print("This game is quite famous,you might have heard of it somehwere or the other. it is called the HANGMAN. LETS BEGIN WITH HANGMAN....\nYou will have to guess the word in just 6 tries. If you guess the word correctly you will win , but if you fail you will be hanged:)...")
          print('''
          88                                                                            
          88                                                                            
          88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba, 8b,dPPYba,
          88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8 88P'    `"8a 
          88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88 88        88
          88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88 88        88
          88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8 88        88
                                              aa,    ,88                                
                                               "Y8bbdP"
          ''')
          random_word = ("committee common company comparison competition complete complex condition connection conscious control existence expansion experience pneumanoultramicroscopicsilicovolcanoconiosis pikachu charizard bulbasour mammorest palworld minecraft gradient gaming computer rubikscube harrypotter avengers fastandfurious paulwalker gamerfleet technogamerz sunshine monday tuesday wednesday thursday friday saturday sunday january february march april september october november december thanos suits fighter").split()
          end_of_game = False
          chosen_word = random.choice(random_word)
          word_length = len(chosen_word)

          #Defining number of lives
          lives = 6

          #Displaying the word in form of blanks
          display = []
          for _ in range(word_length):
              display += "_"

          print("Here is your word, let's see if you can guess this..\n")
          print(display)
          print("\n\n")
          while not end_of_game:
              print(f"You have {lives} lives with you..")
              guess = input("Guess a letter: ").lower()

              #Checking guessed letter
              for position in range(word_length):
                  letter = chosen_word[position]
                  if letter == guess:
                      display[position] = letter

              #Counting number of lives left etc
              if guess not in chosen_word:
                  lives -= 1
                  if lives == 0:
                      end_of_game = True
                      print("Sorry buddy you lost this, but dont feel sad. Better luck next time. Hope you enjoyed playing this game..")
                      print(f"The correct word was {chosen_word}")

              #Join all the elements in the list and turn it into a String.
              print(f"{' '.join(display)}")

              #Check if user has got all letters.
              if "_" not in display:
                  end_of_game = True
                  print("Cudos, you have won this game..")

              print(stages[lives])
hangman()

