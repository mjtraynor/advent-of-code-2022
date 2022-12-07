from pathlib import Path

file_path = './files/'
file_name = 'day3-rucksack-contents.txt'
compartment_1_list = []
compartment_2_list = []
backpack_dict = {}
backpacks_dict = {}
backpack_number = 1
priorities_order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities_total = 0

with open(Path(file_path + file_name), 'r') as file:
    for line in file:
        line_length = len(line.strip())
        for i in range(0, line_length):
            item = line[i]
            if i <= (line_length / 2) - 1:
                compartment_1_list.append(item)
            else:
                 compartment_2_list.append(item)
                 if item in compartment_1_list:
                    duplicate_item = item
        backpack_dict['compartment_1_list'] = compartment_1_list
        backpack_dict['compartment_2_list'] = compartment_2_list
        backpack_dict['duplicate_item'] = duplicate_item
        backpacks_dict['backpack_' + str(backpack_number)] = backpack_dict
        compartment_1_list = []
        compartment_2_list = []
        backpack_dict = {}
        backpack_number += 1

for backpack in backpacks_dict.values():
    duplicate_item = backpack['duplicate_item']
    duplicate_item_priority = priorities_order.rfind(duplicate_item) + 1
    priorities_total += duplicate_item_priority

print(priorities_total)