from pathlib import Path

file_path = './files/'
file_name = 'day2-strategy-guide.txt'
# Convering the letter to the hand shape so that the code is easier to read.
letter_conversion = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
game_dict = {}
games_dict = {}
game_number = 1
my_result = ''
my_game_score = 0
scores = {'rock': 1, 'paper': 2, 'scissors': 3, 'win': 6, 'draw': 3, 'lose': 0}
# Iterate through each line in the file.
with open(Path(file_path + file_name), 'r') as file:
    for line in file:
        # Extract the game letter data and convert it to the hand shape.
        opponent_letter = line.strip()[0]
        my_letter = line.strip()[2]
        opponent_shape = letter_conversion[opponent_letter]
        my_shape = letter_conversion[my_letter]
        # Building a dictionary for each game, and then a dictionary of all games.
        game_dict['opponent_shape'] = opponent_shape
        game_dict['my_shape'] = my_shape
        games_dict['game_' + str(game_number)] = game_dict
        game_dict = {}
        game_number += 1
# Iterate through the games dictionary and extract each game shapes.
for game in games_dict.values():
    opponent_shape = game['opponent_shape']
    my_shape = game['my_shape']
    # Calculate the winenr of each game and add up my score.
    if opponent_shape == my_shape:
        my_result = 'draw'
    elif opponent_shape == 'rock' and my_shape == 'paper':
        my_result = 'win'
    elif opponent_shape == 'paper' and my_shape == 'scissors':
        my_result = 'win'
    elif opponent_shape == 'scissors' and my_shape == 'rock':
        my_result = 'win'
    else:
        my_result = 'lose'

    my_game_score += scores[my_shape]
    my_game_score += scores[my_result]

print('Your total game score is {score}.'.format(score=my_game_score))