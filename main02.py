# Part 1

total_score_part1 = 0
total_score_part2 = 0
win = 6
lost = 0
draw = 3

rock = 1
paper = 2
scissors = 3
duels = open('input02.txt', 'r')

for line in duels.readlines():
    if line[0] == 'A' and line[2] == 'X':
        points = rock + draw
        total_score_part1 += points
    elif line[0] == 'A' and line[2] == 'Y':
        points = paper + win
        total_score_part1 += points
    elif line[0] == 'A' and line[2] == 'Z':
        points = scissors + lost
        total_score_part1 += points
    elif line[0] == 'B' and line[2] == 'X':
        points = rock + lost
        total_score_part1 += points
    elif line[0] == 'B' and line[2] == 'Y':
        points = paper + draw
        total_score_part1 += points
    elif line[0] == 'B' and line[2] == 'Z':
        points = scissors + win
        total_score_part1 += points
    elif line[0] == 'C' and line[2] == 'X':
        points = rock + win
        total_score_part1 += points
    elif line[0] == 'C' and line[2] == 'Y':
        points = paper + lost
        total_score_part1 += points
    elif line[0] == 'C' and line[2] == 'Z':
        points = scissors + draw
        total_score_part1 += points
print(total_score_part1)

# Part 2
duels.seek(0)

for line in duels.readlines():
    if line[0] == 'A' and line[2] == 'X':
        total_score_part2 += scissors + lost
    elif line[0] == 'A' and line[2] == 'Y':
        total_score_part2 += rock + draw
    elif line[0] == 'A' and line[2] == 'Z':
        total_score_part2 += paper + win
    elif line[0] == 'B' and line[2] == 'X':
        total_score_part2 += rock + lost
    elif line[0] == 'B' and line[2] == 'Y':
        total_score_part2 += paper + draw
    elif line[0] == 'B' and line[2] == 'Z':
        total_score_part2 += scissors + win
    elif line[0] == 'C' and line[2] == 'X':
        total_score_part2 += paper + lost
    elif line[0] == 'C' and line[2] == 'Y':
        total_score_part2 += scissors + draw
    elif line[0] == 'C' and line[2] == 'Z':
        total_score_part2 += rock + win

print(total_score_part2)