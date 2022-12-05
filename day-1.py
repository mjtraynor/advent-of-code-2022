from pathlib import Path

file_path = './files/'
file_name = 'day1-calories-list.txt'

individual_calories_list = []
grouped_calories_dict = {}
elf_count = 1
most_calories = {}

# Iterate through each line in the file.
# If it is not a blank line then build a list of calories for that individual elf.
# It it is a blank line then add the elf to the dictionary as a key, and the list
# of calories as the value, then clear the list of calories.
with open(Path(file_path + file_name), 'r') as f:
    for line in f:
        if line.strip() != '':
            individual_calories_list.append(int(line.strip()))
        else:
            grouped_calories_dict['elf_' + str(elf_count)] = individual_calories_list
            individual_calories_list = []
            elf_count += 1
    # If the last line in the file is not blank then add the final elf to the dictionary.
    if len(individual_calories_list) != 0:
        grouped_calories_dict['elf_' + str(elf_count)] = individual_calories_list

# Iterate through each elf in the dictionary.
# If it is the first elf then add the elf and the total calories to the most_calories dictionay.
# If it is not the first elf then check if the total calories is higher than the current highest,
# and if so then replace the elf in the most_calories dictionary.
for elf in grouped_calories_dict:
    total_calories = sum(grouped_calories_dict[elf])
    if not most_calories:
        most_calories = {elf: total_calories}
        elf_with_most_calories = elf
    elif total_calories > most_calories[elf_with_most_calories]:
        most_calories = {elf: total_calories}
        elf_with_most_calories = elf

elf_with_most_calories = list(most_calories.keys())[0]
most_calories_carried = most_calories[elf_with_most_calories]
print('The elf carrying the most calories is {elf} with {calories}.'.format(elf=elf_with_most_calories, calories=most_calories_carried))