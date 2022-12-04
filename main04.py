# Part one
def check_sections(path):
    number_fully_contained_pairs = 0
    sections = open(path, 'r').read().splitlines()

    for line in sections:
        elf1, elf2 = line.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")
        # Change from string to int
        elf1_start_int = int(elf1_start)
        elf2_start_int = int(elf2_start)
        elf1_end_int = int(elf1_end)
        elf2_end_int = int(elf2_end)

        if elf1_start_int <= elf2_start_int and elf1_end_int >= elf2_end_int:
            number_fully_contained_pairs += 1
        elif elf2_start_int <= elf1_start_int and elf2_end_int >= elf1_end_int:
            number_fully_contained_pairs += 1
    print(number_fully_contained_pairs)


check_sections('input04.txt')

# Part 2

def evaluate_section(section1_start, section1_end, section2_start, section2_end):
    for i in range(section1_start, section1_end + 1):
        for j in range(section2_start, section2_end + 1):
            if i == j:
                return True
    return False

def check_overlapping(path):
    number_of_overlapped_pairs = 0
    sections = open(path, 'r').read().splitlines()

    for line in sections:
        elf1, elf2 = line.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")
        # Change from string to int
        elf1_start_int = int(elf1_start)
        elf2_start_int = int(elf2_start)
        elf1_end_int = int(elf1_end)
        elf2_end_int = int(elf2_end)

        if evaluate_section(elf1_start_int, elf1_end_int, elf2_start_int, elf2_end_int):
            number_of_overlapped_pairs += 1
    print(number_of_overlapped_pairs)

check_overlapping('input04.txt')