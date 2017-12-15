from datetime import datetime


def day_18():
    puzzle_loc = '.txt'

    def puzzle_1(input_str):
        pass
    yield puzzle_1(puzzle_loc)

    def puzzle_2(input_str):
        pass
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_18 in day_18():
    print(solution_18)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

