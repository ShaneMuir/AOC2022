from aocd.models import Puzzle
from aocd import submit

day_2 = Puzzle(year=2022, day=2)
my_data = day_2.input_data  # Gets our puzzle input


def puzzle_two():
    our_score = 0
    for i in my_data.split('\n'):
        opponent, you = i.split()

        if you == "X":
            if opponent == "C":
                our_score += 6
            if opponent == "A":
                our_score += 3
            our_score += 1

        if you == "Y":
            if opponent == "A":
                our_score += 6
            if opponent == "B":
                our_score += 3
            our_score += 2

        if you == "Z":
            if opponent == "B":
                our_score += 6
            if opponent == "C":
                our_score += 3
            our_score += 3

    print(our_score)


# puzzle_two()

def puzzle_two_part_two():
    our_score = 0
    for i in my_data.split("\n"):
        opponent, you = i.split()

        if you == "X":
            if opponent == "A":
                our_score += 3
            if opponent == "B":
                our_score += 1
            if opponent == "C":
                our_score += 2

            our_score += 0

        if you == "Y":
            if opponent == "A":
                our_score += 1
            if opponent == "B":
                our_score += 2
            if opponent == "C":
                our_score += 3
            our_score += 3

        if you == "Z":
            if opponent == "A":
                our_score += 2
            if opponent == "B":
                our_score += 3
            if opponent == "C":
                our_score += 1
            our_score += 6

    print(our_score)


puzzle_two_part_two()
