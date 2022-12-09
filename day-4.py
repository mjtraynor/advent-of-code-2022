from pathlib import Path

def main():
    file_path = './files/'
    file_name = 'day4-section-assignment.txt'

    assignments = create_assignment_dict(file_path=file_path, file_name=file_name)
    full_duplication_count = duplicate_section_check(assignments_dict=assignments)
    overlap_count = overlap_section_check(assignments_dict=assignments)

    print('There are {assignment_count} assignments with full duplication of sections.'.format(assignment_count=full_duplication_count))
    print('There are {overlap_count} assignments with an overlap of sections.'.format(overlap_count=overlap_count))
    print(assignments)

def create_assignment_dict(file_path:str, file_name: str) -> dict:
    assignment_dict = {}
    assignments_dict = {}

    with open(Path(file_path + file_name), 'r') as file:
        assignment = 1
        # Iterate through each line in the file.
        for line in file:
            # Build a dictionary of lists for each section.
            section = 1
            assignment_split = line.strip().split(',')
            for item in assignment_split:
                section_split = item.split('-')
                assignment_dict['section_{section}'.format(section=str(section))] = section_split

                section += 1
            # Add the asignment dictionary to a dictionary of assignments.
            assignments_dict['assignment_{assignment}'.format(assignment=str(assignment))] = assignment_dict
            assignment_dict = {}        
            assignment += 1
    
    return assignments_dict

def duplicate_section_check(assignments_dict: dict) -> int:
    full_duplication_count = 0
    # Iterate through the assignments.
    for assignment in assignments_dict.values():
        # Extract the section start and ends as integers.
        full_dupliction = False
        section_1_start = int(assignment['section_1'][0])
        section_1_end = int(assignment['section_1'][1])
        section_2_start = int(assignment['section_2'][0])
        section_2_end = int(assignment['section_2'][1])
        # Check if the first sections start and end number are within the second section, and vice versa.
        # If so then add a flag to the assignment dictionary and increase the duplication count.
        if (section_1_start >= section_2_start and section_1_end <= section_2_end) or \
            (section_2_start >= section_1_start and section_2_end <= section_1_end):

            full_dupliction = True
            full_duplication_count += 1

        assignment['full_duplication'] = full_dupliction
        
    return full_duplication_count

def overlap_section_check(assignments_dict: dict) -> int:
    overlap_count = 0
    # Iterate through the assignments.
    for assignment in assignments_dict.values():
        # Extract the section start and ends as integers.
        overlap = False
        section_1_start = int(assignment['section_1'][0])
        section_1_end = int(assignment['section_1'][1])
        section_2_start = int(assignment['section_2'][0])
        section_2_end = int(assignment['section_2'][1])
        # Iterate through the range of the first section and check if it is in the range of the second section.
        for item in range(section_1_start, section_1_end + 1):
            # When a number from the first section is in the second section then add a flag to the assignment
            # dictionary, increase the overlap count, and then exit out the loop and move onto the next assignment.
            if item in range(section_2_start, section_2_end + 1):
                overlap = True
                overlap_count += 1
                break
        continue

        assignment['overlap'] = overlap
        
    return overlap_count

if __name__ == "__main__":
    main()