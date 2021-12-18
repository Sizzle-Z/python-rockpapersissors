import random

# Defined Variables
options = ['Rock', 'Paper', 'Sissors']
ai_selection = random.choice(options)

# User Input
user_selection = input('Select rock, paper, or sissors! ')
user_selection_lower = user_selection.lower()

# Check who won
if ai_selection == user_selection: print('There was a tie!')
if ai_selection == 'Rock' and user_selection_lower == 'sissors': print('You lost! The AI chose ' + ai_selection)
if ai_selection == 'Sissors' and user_selection_lower == 'rock': print('You won! The AI chose ' + ai_selection)
if ai_selection == 'Sissors' and user_selection_lower == 'paper': print('You lost! The AI chose ' + ai_selection)
if ai_selection == 'Paper' and user_selection_lower == 'sissors': print('You won! The AI chose ' + ai_selection)
if ai_selection == 'Paper' and user_selection_lower == 'rock': print('You lost! The AI chose ' + ai_selection)
if ai_selection == 'Rock' and user_selection_lower == 'paper': print('You won! The AI chose ' + ai_selection)
