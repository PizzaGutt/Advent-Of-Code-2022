# Part 1
most_calories = 0
current_calories = 0
f = open('input01.txt', 'r')

for line in f.readlines():
    if line != '\n':
        current_calories += int(line)
    else:
        if current_calories > most_calories:
            most_calories = current_calories
            current_calories = 0
        current_calories = 0

print(most_calories)

# Part 2
f.seek(0)

most_calories = 0
second_most_calories = 0
third_most_calories = 0
current_calories = 0
f = open('input01.txt', 'r')

for line in f.readlines():
    if line != '\n':
        current_calories += int(line)
    else:
        if current_calories > most_calories:
            second_most_calories = most_calories
            most_calories = current_calories
        elif current_calories > second_most_calories:
            third_most_calories = second_most_calories
            second_most_calories = current_calories
        elif current_calories > third_most_calories:
            third_most_calories = current_calories
        current_calories = 0

top_three_total = most_calories + second_most_calories + third_most_calories
print(top_three_total)
