from pathlib import Path

file_path = './files/'
file_name = 'day2-strategy-guide.txt'
game_dict = {}
games_dict = {}
game_number = 1

with open(Path(file_path + file_name), 'r') as file:
    # Iterate through each line in the file.
    for line in file:
        # Extract the game letter data.
        opponent_letter = line.strip()[0]
        my_letter = line.strip()[2]
        # Build a dictionary for each game, and then a dictionary of all games.
        game_dict['opponent_letter'] = opponent_letter
        game_dict['my_letter'] = my_letter
        games_dict['game_' + str(game_number)] = game_dict
        game_dict = {}
        game_number += 1

def calculate_game_score(conversion_type: str):
    opponent_conversion_shape = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    my_conversion_shape = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    my_conversion_result = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    win_lose_dict = {'paper': 'rock', 'rock': 'scissors', 'scissors': 'paper'}
    scores = {'rock': 1, 'paper': 2, 'scissors': 3, 'win': 6, 'draw': 3, 'lose': 0}
    my_game_score = 0

    for game in games_dict.values():
        opponent_shape = opponent_conversion_shape[game['opponent_letter']]
        # Calculate my result if my letter is converts to a shape.
        if conversion_type == 'shape':
            my_shape = my_conversion_shape[game['my_letter']]
            if opponent_shape == my_shape:
                my_result = 'draw'
            elif my_shape == win_lose_dict[opponent_shape]:
                my_result = 'lose'
            else:
                my_result = 'win'
        # Calculate my shape if my letter is converts to a result.
        elif conversion_type == 'result':
            my_result = my_conversion_result[game['my_letter']]
            if my_result == 'draw':
                my_shape = opponent_shape
            elif my_result == 'lose':
                my_shape = win_lose_dict[opponent_shape]
            else:
                my_shape = [i for i in win_lose_dict if win_lose_dict[i] == opponent_shape][0]

        my_game_score += scores[my_shape]
        my_game_score += scores[my_result]

    return my_game_score

def main():
    game_score_shape = calculate_game_score('shape')
    game_score_result = calculate_game_score('result')

    print('Using the letters as shapes, your total game score is {score}.'.format(score=game_score_shape))
    print('Using the letters as results, your total game score is {score}.'.format(score=game_score_result))

if __name__ == '__main__':
    main()