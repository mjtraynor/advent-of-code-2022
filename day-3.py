from pathlib import Path

def main():
    file_path = './files/'
    file_name = 'day3-rucksack-contents.txt'
    priorities_order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    backpacks_dict = create_backpacks_dict(file_path=file_path, file_name=file_name)
    
    priority = calculate_priorities(backpacks_dict=backpacks_dict, priorities_order=priorities_order)
    group_priority = calculate_group_priorities(backpacks_dict=backpacks_dict, priorities_order=priorities_order)

    print('The priorities total for all the duplicate items is {priorities}.'.format(priorities=priority))
    print('The group priorities total for all the common items is {priorities}.'.format(priorities=group_priority))

def create_backpacks_dict(file_path: str, file_name: str) -> dict:
    compartment_1_list = []
    compartment_2_list = []
    backpack_dict = {}
    backpacks_dict = {}
    backpack_number = 1

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

    return backpacks_dict

def calculate_priorities(backpacks_dict: dict, priorities_order: str) -> int:
    priorities_total = 0

    for backpack in backpacks_dict.values():
        duplicate_item = backpack['duplicate_item']
        duplicate_item_priority = priorities_order.rfind(duplicate_item) + 1
        priorities_total += duplicate_item_priority

    return priorities_total

def calculate_group_priorities(backpacks_dict: dict, priorities_order: str) -> int:
    grouped_list = []
    priorities_total = 0

    for i in range (0, len(backpacks_dict)):
        backpack = backpacks_dict['backpack_' + str(i + 1)]
        backpack_unique_items = list(set(backpack['compartment_1_list'] + backpack['compartment_2_list']))
        if i == 0 or i % 3 != 0:
            grouped_list.append(backpack_unique_items)
        else:
            common_item = set(grouped_list[0]).intersection(grouped_list[1]).intersection(grouped_list[2]).pop()
            backpack['common_item'] = common_item
            duplicate_item_priority = priorities_order.rfind(common_item) + 1
            priorities_total += duplicate_item_priority
            if i != len(backpacks_dict):
                grouped_list = [backpack_unique_items]
            
    common_item = set(grouped_list[0]).intersection(grouped_list[1]).intersection(grouped_list[2]).pop()
    backpack['common_item'] = common_item
    duplicate_item_priority = priorities_order.rfind(common_item) + 1
    priorities_total += duplicate_item_priority

    return priorities_total

if __name__ == "__main__":
    main()