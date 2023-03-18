import random

def draw_letters():
    # Letters to choose from
    LETTER_POOL = {
        'A': 9, 
        'B': 2, 
        'C': 2, 
        'D': 4, 
        'E': 12, 
        'F': 2, 
        'G': 3, 
        'H': 2, 
        'I': 9, 
        'J': 1, 
        'K': 1, 
        'L': 4, 
        'M': 2, 
        'N': 6, 
        'O': 8, 
        'P': 2, 
        'Q': 1, 
        'R': 6, 
        'S': 4, 
        'T': 6, 
        'U': 4, 
        'V': 2, 
        'W': 2, 
        'X': 1, 
        'Y': 2, 
        'Z': 1
    }

    ten_letters = [] # List for 10 random letters

    # While list length < 10, pick random letter from dictionary for list
    while len(ten_letters) < 10:
        letter_to_add = random.choice(list(LETTER_POOL))

        # Check that letter is still available in LETTER_POOL
        # Add available letter to ten_letters
        # Decrement count of letter by 1 after use
        if LETTER_POOL.get(letter_to_add) > 0:
            ten_letters.append(letter_to_add)
            LETTER_POOL[letter_to_add] -= 1

    return ten_letters

def uses_available_letters(word, letter_bank):
    letter_bank_dict = {}
    word = word.upper()

    for letter in letter_bank:
        if letter in letter_bank_dict:
            letter_bank_dict[letter] += 1 # Increment count of letter by 1
        else:
            letter_bank_dict[letter] = 1 # Add new pair with letter and 1

    for letter in word:
        if not letter in letter_bank_dict or letter_bank_dict[letter] == 0:
            return False # Not an anagram of letters in letter_bank
        
        letter_bank_dict[letter] -= 1 # Decrement key's value by 1
    
    return True

def score_word(word):
    # Dictionary of letters and points
    letter_scores = {
        'A': 1,
        'E': 1,
        'I': 1,
        'O': 1,
        'U': 1,
        'L': 1,
        'N': 1,
        'R': 1,
        'S': 1,
        'T': 1,
        'D': 2,
        'G': 2,
        'B': 3,
        'C': 3,
        'M': 3,
        'P': 3,
        'F': 4,
        'H': 4,
        'V': 4,
        'W': 4,
        'Y': 4,
        'K': 5,
        'J': 8,
        'X': 8,
        'Q': 10,
        'Z': 10
    }

    word_score = 0
    word = word.upper() # Convert word to uppercase letters

    # Check if the word length rewards an extra 8 points
    if len(word) in (7, 8, 9, 10):
        word_score += 8

    # Add value of each letter in word to word_score total
    for letter in word:
        if letter in letter_scores:
            word_score += letter_scores[letter]
    
    return word_score


def get_highest_word_score(word_list):
    pass