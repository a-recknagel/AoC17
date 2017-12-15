from datetime import datetime


def day_22():
    puzzle_loc = '.txt'

    def puzzle_1(input_str):
        pass
    yield puzzle_1(puzzle_loc)

    def puzzle_2(input_str):
        pass
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_22 in day_22():
    print(solution_22)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

