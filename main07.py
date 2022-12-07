file = open('input07.txt').read().splitlines()
current_directory = []
directories_in_the_system = {"/": 0}
total = 0

for line in file:
    if "$ cd .." == line:
        current_directory.pop()

    elif "$ cd" in line:
        dollar, command, go_to_directory = line.split(" ")
        current_directory.append(go_to_directory)

    elif "dir" == line[0:3]:
        dir_name = ""
        for direct in current_directory:
            dir_name += direct
        dir_name += line[4:]
        if dir_name not in directories_in_the_system:
            directories_in_the_system[dir_name] = 0

    elif line[0].isnumeric():
        size, file = line.split(" ")
        current_dir = ""
        for direct2 in current_directory:
            current_dir += direct2
            directories_in_the_system[current_dir] += int(size)

# Part One

# reversed_dict = {}
# for key in reversed(directories_in_the_system):
#     reversed_dict[key] = directories_in_the_system[key]
#
#
# for directory in reversed_dict:
#     if directories_in_the_system[directory] <= 100000:
#         total += directories_in_the_system[directory]

# Part Two.

space_available = 70000000 - directories_in_the_system['/']
space_needed = 30000000 - space_available
can_delete = []

for key in directories_in_the_system:
    if directories_in_the_system[key] >= space_needed:
        can_delete.append(directories_in_the_system[key])

lowest = min(can_delete)
print(lowest)
