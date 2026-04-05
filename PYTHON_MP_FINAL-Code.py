import random

def making_a_guess():
    try:
        x = 0
        global update_display
        correct_guess = False
        
        # Validate input
        if not guess or len(guess) == 0:
            raise ValueError("Please enter a valid letter!")
        
        if len(guess) > 1:
            raise ValueError("Please enter only ONE letter at a time!")
        
        if not guess.isalpha():
            raise ValueError("Please enter only alphabetic characters!")
        
        for letter in chosen_word:
            if guess.lower() == chosen_word[x]:
                blank_list[x] = guess.lower()
                correct_guess = True
            x += 1
        
        if correct_guess == False:
            print(f"❌ There is no '{guess}', sorry.")
            update_display += 1
        else:
            print(f"✓ Good guess! '{guess}' is in the word.")
        x = 0
        
    except ValueError as ve:
        print(f"⚠️  Input Error: {ve}")
    except Exception as e:
        print(f"⚠️  An unexpected error occurred: {e}")


def get_hint():
    try:
        word_str = ''.join(chosen_word)
        
        if word_str not in word_hints:
            raise KeyError(f"No hint available for '{word_str}'")
        
        hint = word_hints[word_str]
        print(f"💡 Hint: {hint}")
        
    except KeyError as ke:
        print(f"⚠️  {ke}")
    except Exception as e:
        print(f"⚠️  Error retrieving hint: {e}")


HANGMANPICS = ['''
  +---+
  !   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Dictionary with words and their hints
word_hints = {
    "aardvark": "A burrowing African mammal that starts with 'A'",
    "baboon": "A large primate found in Africa",
    "camel": "A desert animal with humps",
    "jazz": "A music genre known for improvisation",
    "grass": "Green plant that covers lawns",
    "follow": "To go after someone or something",
    "castle": "A large fortified building",
    "cloud": "A white fluffy thing in the sky"
}

word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]

try:
    chosen_word = list(random.choice(word_list))
    
    blank = ""
    for letter in chosen_word:
        blank += "_"
    blank_list = list(blank)
    
    update_display = 0
    hints_used = 0
    max_hints = 2
    
    print(HANGMANPICS[update_display])
    print(f"\n{''.join(blank_list)}")
    print(f"(You have {max_hints} hints available)\n")
    
    while True:
        try:
            user_input = input("Make a guess (or type 'hint' for a clue): ").strip()
            
            if user_input.lower() == 'hint':
                if hints_used < max_hints:
                    hints_used += 1
                    get_hint()
                    print(f"Hints remaining: {max_hints - hints_used}\n")
                else:
                    print(f"❌ No hints remaining! You've used all {max_hints} hints.\n")
                continue
            
            guess = user_input
            making_a_guess()
            
        except KeyboardInterrupt:
            print("\n\n👋 Game interrupted by user. Thanks for playing!")
            exit()
        except Exception as e:
            print(f"⚠️  Error during guess: {e}\n")
            continue
        
        print(HANGMANPICS[update_display])
        print(''.join(blank_list))
        
        # Check win condition
        if blank_list == chosen_word:
            print("\n🎉 YOU WIN! Congratulations! 🎉")
            print(f"The word was: {''.join(chosen_word)}")
            break
        
        # Check lose condition
        if update_display == 6:
            print("\n😢 GAME OVER. You lost!")
            print(f"The word was: {''.join(chosen_word)}")
            break

except Exception as e:
    print(f"❌ Fatal error: {e}")
    print("The game could not start. Please try again.")