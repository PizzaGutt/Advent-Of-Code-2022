
def make_stacks(path):
    crates = []
    for line in open(path, 'r').readlines():
        if line == "\n":
            break
        else:
            crates.append(line.replace("\n", ""))

    crate_list = []
    counter = 1
    while counter <= int(crates[-1][-2]):
        for l in crates[::-1]:
            current_stack = []
            if str(counter) in l:
                letter_index = l.find(str(counter))
                for _ in crates:
                    if len(_) < letter_index or _[letter_index] == " ":
                        continue
                    else:
                        current_stack.append(_[letter_index])
                current_stack.pop()
            if len(current_stack) != 0:
                current_stack.reverse()
                crate_list.append(current_stack)
        counter += 1
    return crate_list

def instructions(path):
    instructs = []
    for line in open(path, 'r').readlines():
        if line[0] == 'm':
            instructs.append(line.replace("\n", "").split(" "))

    for _ in instructs:
        for item in _:
            if not item.isnumeric():
                _.remove(item)
    return instructs


stacks = make_stacks('input05.txt')
instruction = instructions('input05.txt')

for instruct in instruction:
    move_count = int(instruct[0])
    current_place = int(instruct[1])
    to_place = int(instruct[2])
    for i in range(move_count, 0, -1):
        # stacks[to_place-1].append(stacks[current_place - 1][-1]) (Part 1)
        # stacks[current_place-1].pop(-1)
        stacks[to_place - 1].append(stacks[current_place - 1][-i])
        stacks[current_place-1].pop(-i)
answer = ""
for stack in stacks:
    answer += stack[-1]

# print(answer) Part 1 Code
print(answer) # Part 2 Code