from datetime import datetime


def day_17():
    puzzle_loc = '.txt'

    def puzzle_1(input_str):
        pass
    yield puzzle_1(puzzle_loc)

    def puzzle_2(input_str):
        pass
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_17 in day_17():
    print(solution_17)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

