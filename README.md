# Hangman Game 🎮

A simple Python Hangman game with hints and error handling.

## Features

### 1. **Hint Dictionary**
- Each word has a hint stored in a dictionary
- Players can type `'hint'` to get a clue about the word
- Limited to 2 hints per game

**Example:**
```python
word_hints = {
    "aardvark": "A burrowing African mammal that starts with 'A'",
    "camel": "A desert animal with humps",
}
```

### 2. **Exception Handling (Try/Except)**
- **Input Validation**: Checks if the player enters valid letters (not numbers or special characters)
- **Error Messages**: Shows friendly messages if something goes wrong
- **Game Safety**: Prevents the game from crashing due to invalid input

**Example:**
```python
try:
    if not guess.isalpha():
        raise ValueError("Please enter only alphabetic characters!")
except ValueError as ve:
    print(f"⚠️ Input Error: {ve}")
```

### 3. **How to Play**
1. Run the game
2. Guess one letter at a time
3. Type `'hint'` to get a clue (you have 2 hints)
4. Complete the word before the hangman is drawn
5. Win by guessing the word or lose if you run out of tries

### 4. **Game Elements**
- **Word List**: 8 different words to guess from
- **Attempts**: 6 wrong guesses allowed
- **Visual Feedback**: ASCII art shows your progress
- **Smart Messages**: Tells you if a letter is correct or wrong

## Installation

```bash
python hangman_improved.py
```

## Code Highlights

### Hint Function
Safely retrieves hints from the dictionary with error handling:
```python
def get_hint():
    try:
        word_str = ''.join(chosen_word)
        if word_str not in word_hints:
            raise KeyError(f"No hint available for '{word_str}'")
        hint = word_hints[word_str]
        print(f"💡 Hint: {hint}")
    except KeyError as ke:
        print(f"⚠️ {ke}")
```

### Guess Validation
Checks for valid input before processing:
```python
if not guess or len(guess) == 0:
    raise ValueError("Please enter a valid letter!")
if len(guess) > 1:
    raise ValueError("Please enter only ONE letter!")
if not guess.isalpha():
    raise ValueError("Please enter only alphabetic characters!")
```

## Author
Created as a fun learning project for Python beginners!
