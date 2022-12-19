from pathlib import Path

def main():
    file_path = './files/'
    file_name = 'day6-datastream-buffer.txt'

    buffer = get_buffer(file_path=file_path, file_name=file_name)

    packet_marker = get_buffer_marker(buffer=buffer, marker_type='packet')

    if packet_marker == -1:
        print('The buffer does not contain a valid packet marker.')
    else:
        print('The buffers packet marker is at position {position}.'.format(position=packet_marker))

    message_marker = get_buffer_marker(buffer=buffer, marker_type='message')

    if message_marker == -1:
        print('The buffer does not contain a valid message marker.')
    else:
        print('The buffers message marker is at position {position}.'.format(position=message_marker))

def get_buffer(file_path:str, file_name: str) -> str:
    buffer = ''

    with open(Path(file_path + file_name), 'r') as file:
        # Iterate through each line in the file and concatenate each line as text.
        for line in file:
            buffer += line.strip()

        return buffer

def get_buffer_marker(buffer: str, marker_type: str) -> int:
    start = 0
    if marker_type == 'packet':
        end = 4
    elif marker_type == 'message':
        end = 14
    # Iterate through each letter in the buffer.
    for i in range(4, len(buffer) + 1):
        # Create a variable to hold each running 4 character string and check if the
        # length of the string is the same as the number of unique characters. If it
        # is then return the position of the last character pulled from the buffer
        # and exit out the loop.
        text_check = buffer[start: end]
        unique_chars = len(set(text_check)) == len(text_check)
        if unique_chars:
            return end

        start += 1
        end += 1
    # If the loop reaches the end of the buffer then return -1 as a check value.
    return -1

if __name__ == '__main__':
    main()