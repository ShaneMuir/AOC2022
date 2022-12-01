from aocd.models import Puzzle
from aocd import submit

day_1 = Puzzle(year=2022, day=1)
my_data = day_1.input_data

def puzzle_one():
    """
    Method to solve puzzle one
    """

    # Here I split the input into a list of strings including the new line
    data = [i for i in my_data.strip().split('\n')]

    max_kcals = 0
    kcals = 0
    for item in data:
        if item == '':
            kcals = 0 # For each new line reset kcal counter
        else:
            item_num = int(item) # Convert string line into int for addition
            kcals += item_num # Adds each line up until we hit a new line

        if kcals > max_kcals:
            max_kcals = kcals # If new kcal count is bigger then any previous elf's kcals record it

    submit(max_kcals, part='a', day=1, year=2022)

puzzle_one()