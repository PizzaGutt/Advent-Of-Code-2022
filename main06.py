#
# alphabet = ""
# file = open('test-06.txt').read()
# index = 0
# characters_before_mark = 0

# Part one
# while True:
#     alphabet += file[index:index+4]
#     for idx in range(4):
#         if alphabet.count(alphabet[idx]) > 1:
#             alphabet = ""
#             characters_before_mark += 1
#             index += 1
#             break
#     if len(alphabet) == 4:
#         print(characters_before_mark + 4)
#         break

# Part 2
alphabet = ""
file = open('input06.txt').read()
index = 0
characters_before_mark = 0

while True:
    alphabet += file[index:index+14]
    for idx in range(14):
        if alphabet.count(alphabet[idx]) > 1:
            alphabet = ""
            characters_before_mark += 1
            index += 1
            break
    if len(alphabet) == 14:
        print(characters_before_mark + 14)
        break
