# Part 1

dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
              'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
              't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28,
              'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
              'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46,
              'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}

def checkBackPack(path):
    total_score = 0
    f = open(path, 'r')
    backpacks = f.read().splitlines()
    for backpack in backpacks:
        main_letter = "+"
        equal_value_items = len(backpack) // 2
        backpack_part1 = backpack[:equal_value_items]
        backpack_part2 = backpack[equal_value_items:]
        for letter in backpack_part1:
            if letter in backpack_part2:
                if backpack.count(letter) > backpack.count(main_letter):
                    main_letter = letter
        total_score += dictionary[main_letter]
    return total_score


print(checkBackPack('input03.txt'))

# Part 2
def checkBadge(path):
    total_score = 0
    counter = 0
    f = open(path, 'r')
    backpacks = f.read().splitlines()

    while True:
        main_letter_count = 0
        if counter == len(backpacks):
            return total_score
        line_1 = backpacks[counter]
        line_2 = backpacks[counter + 1]
        line_3 = backpacks[counter + 2]

        main_letter2 = "+"
        for letter in line_1:
            if letter in line_2 and letter in line_3:
                line1_letter_count = line_1.count(letter)
                line2_letter_count = line_2.count(letter)
                line3_letter_count = line_3.count(letter)
                total_letter_count = line1_letter_count + line2_letter_count + line3_letter_count
                if total_letter_count > main_letter_count:
                    main_letter2 = letter
                    main_letter_count = total_letter_count

        total_score += dictionary[main_letter2]
        counter += 3


print(checkBadge('input03.txt'))




