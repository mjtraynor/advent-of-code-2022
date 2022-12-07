from pathlib import Path

file_path = './files/'
file_name = 'day1-calories-list.txt'
individual_calories_list = []
grouped_calories_dict = {}
elf_count = 1
most_calories_list = []

with open(Path(file_path + file_name), 'r') as file:
    # Iterate through each line in the file.
    for line in file:
        # If it is not a blank line then build a list of calories for that individual elf.
        if line.strip() != '':
            individual_calories_list.append(int(line.strip()))
        # It it is a blank line then add the elf to the dictionary as a key, and the list
        # of calories as the value, then clear the list of calories.
        else:
            grouped_calories_dict['elf_' + str(elf_count)] = individual_calories_list
            individual_calories_list = []
            elf_count += 1
    # If the last line in the file is not blank then add the final elf to the dictionary.
    if len(individual_calories_list) != 0:
        grouped_calories_dict['elf_' + str(elf_count)] = individual_calories_list

# Sort the grouped calories dictionary by total calories in ascending order.
sorted_grouped_calories_list = sorted(grouped_calories_dict.items(), key=lambda kv: sum(kv[1]))

# Pop off the top 3 into a new list.
for i in range(0, 3):
    most_calories_list.append(sorted_grouped_calories_list.pop())

elf_with_most_calories = most_calories_list[0][0]
most_calories = sum(most_calories_list[0][1])
top_three_calories = sum([sum(item[1]) for item in most_calories_list])

print('The elf carrying the most calories is {elf} with {calories} calories.'.format(
    elf=elf_with_most_calories, calories=most_calories
))
print('The 3 elfs carrying the most calories have a combined total of {calories} calories.'.format(
    calories=top_three_calories
))