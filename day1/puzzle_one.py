from aocd.models import Puzzle
from aocd import submit

day_1 = Puzzle(year=2022, day=1)
my_data = day_1.input_data

# Here I split the input into a list of strings including the new line
data = [i for i in my_data.strip().split('\n')]


def puzzle_one():
    """
    Method to solve puzzle one
    """

    max_kcals = 0
    count = 0
    for item in data:
        if item == '':
            count = 0  # For each new line reset kcal counter
        else:
            item_num = int(item)  # Convert string line into int for addition
            count += item_num  # Adds each line up until we hit a new line

        if count > max_kcals:
            max_kcals = count  # If new kcal count is bigger then any previous elf's kcals record it

    # print("Max Elf Kcals:", max_kcals)
    submit(max_kcals, part='a', day=1, year=2022)


# puzzle_one()

def puzzle_one_part_two():
    """
    Method to solve puzzle one part 2
    """
    kcals_one = 0
    kcals_two = 0
    kcals_three = 0
    counter = 0

    for item in data:
        if item == "":
            counter = 0
        else:
            num = int(item)
            counter += num

        if counter > kcals_one:
            kcals_one = counter
        elif counter > kcals_two:
            kcals_two = counter
        elif counter > kcals_three:
            kcals_three = counter

    total_kcals = kcals_one + kcals_two + kcals_three

    submit(total_kcals, part='b', day=1, year=2022)

# puzzle_one_part_two()
