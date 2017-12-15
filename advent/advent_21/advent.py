from datetime import datetime


def day_21():
    puzzle_loc = '.txt'

    def puzzle_1(input_str):
        pass
    yield puzzle_1(puzzle_loc)

    def puzzle_2(input_str):
        pass
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_21 in day_21():
    print(solution_21)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

