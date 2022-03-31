import os

command = input().split('-')

while not command[0] == 'End':

    file_name = command[1]

    if command[0] == 'Create':
        open(file_name, 'w').close()

    elif command[0] == 'Add':
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(f'{content} \n')

    elif command[0] == 'Replace':
        old_string, new_string = command[2], command[3]
        replaced_content = []
        lines_count = 0

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    replaced_content.append(line.replace(old_string, new_string))
                    lines_count += 1
            with open(file_name, 'r+') as file:
                for i in range(lines_count):
                    file.write(replaced_content[i])
        except FileNotFoundError:
            print('An error occurred')

    elif command[0] == 'Delete':

        try:
            os.remove(file_name)
        except FileNotFoundError:
            print('An error occurred')

    command = input().split('-')


# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End