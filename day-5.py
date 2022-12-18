from pathlib import Path

def main():
    file_path = './files/'
    file_name = 'day5-crate-stacks.txt'

    moves_dict = create_moves_dict(file_path=file_path, file_name=file_name)


    crane_type = '9000'
    stack_dict = move_crates(file_path=file_path, file_name=file_name, moves_dict=moves_dict, crane_type=crane_type)
    top_crates = get_top_crates(stack_dict=stack_dict)
    print('Using the {crane_type} crane, the crates at the top of the stack \
        are {crates}.'.format(crane_type=crane_type, crates=top_crates))

    crane_type = '9001'
    stack_dict = move_crates(file_path=file_path, file_name=file_name, moves_dict=moves_dict, crane_type=crane_type)
    top_crates = get_top_crates(stack_dict=stack_dict)
    print('Using the {crane_type} crane, the crates at the top of the stack \
        are {crates}.'.format(crane_type=crane_type, crates=top_crates))
    

def create_initial_stacks(file_path:str, file_name: str) -> dict:
    # Initialise a dictionary for each stack.
    stacks_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    # Create a dicionary that indicated what stack to put the letter in, depending on the
    # character in the line.
    file_stack_dict = {1: 1, 5: 2, 9: 3, 13: 4, 17: 5, 21: 6, 25: 7, 29: 8, 33: 9}

    with open(Path(file_path + file_name), 'r') as file:
        # Iterate through each line in the file.
        for line in file:
            if '1' not in line:
                for i in range(0, len(line.strip())):
                    # Check if the character position is in the dictionary, and if so then
                    # add the letter to the correct stack.
                    if i in file_stack_dict:
                        stack = file_stack_dict[i]
                        crate = line.strip()[i]
                        stacks_dict[stack].append(crate)
            # Break out the file iteration when the line contains '1'.
            else:
                break
        
        for stack in stacks_dict.values():
            # Reverse the stacks so that the top crate is at th end of the list.
            stack.reverse()
            # Remove all the crates that are blank.
            stack[:] = [crate for crate in stack if crate != ' ']
        
        return stacks_dict

def create_moves_dict(file_path:str, file_name: str) -> dict:
    move_dict = {}
    moves_dict = {}
    move_number = 1
    # Iterate through the file.
    with open(Path(file_path + file_name), 'r') as file:
        for line in file:
            if 'move' in line:
                # Remove the words from the line and add turn the numbers into a list.
                line_list = line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
                # Add the numbers to the move dictionary.
                move_dict['move'] = int(line_list[0])
                move_dict['from'] = int(line_list[1])
                move_dict['to'] = int(line_list[2])
                # Add the move dictionary to the moves dictionary.
                moves_dict['move_' + str(move_number)] = move_dict
                move_dict = {}
                move_number += 1

    return moves_dict

#def move_crates(stack_dict: dict, moves_dict: dict, crane_type: str) -> dict:
def move_crates(file_path: str, file_name: str, moves_dict: dict, crane_type: str) -> dict:
    stack_dict = create_initial_stacks(file_path=file_path, file_name=file_name)
    for move_dict in moves_dict.values():
        temp_stack = []
        # Extract the move details from the dictionary.
        move_int = move_dict['move']
        from_int = move_dict['from']
        to_int = move_dict['to']
        # Remove the crates from the 'from' stack and add them to a temp stack.
        for i in range(0, move_int):
            temp_stack.append(stack_dict[from_int].pop())
        # If we are using the 9001 crane then reverse the temp stack.
        temp_stack.reverse() if crane_type == '9001' else ...
        # Add each crate in the temp stack to the 'to' stack.
        for crate in temp_stack:
            stack_dict[to_int].append(crate)

    return stack_dict

def get_top_crates(stack_dict: dict) -> str:
    top_crates = ''
    # Extart the top crate from each stack and add it to the string.
    for stack in stack_dict.values():
        top_crates += stack[-1]

    return top_crates

if __name__ == "__main__":
    main()