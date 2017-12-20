from datetime import datetime


def day_19():
    puzzle_loc = 'paths.txt'

    def next_dir(tubes, current_loc, current_dir):
        for test in [[current_dir[1], current_dir[0]],
                     [current_dir[1] * -1, current_dir[0] * -1]]:
            try:
                tmp = tubes[current_loc[0] + test[0]][current_loc[1] + test[1]]
            except IndexError:
                continue
            if tmp != ' ':
                return test

    def walk_grid(tubes):
        chars = ''
        current_loc = [0, tubes[0].index('|')]
        current_dir = [1, 0]
        count = 0
        while tubes[current_loc[0]][current_loc[1]] != 'F':
            count += 1
            tmp = tubes[current_loc[0]][current_loc[1]]
            if tmp == '|' or tmp == '-':
                pass
            elif tmp == '+':
                current_dir = next_dir(tubes, current_loc, current_dir)
            else:  # tmp in [A-Z]
                chars += tmp
            current_loc[0] += current_dir[0]
            current_loc[1] += current_dir[1]
        return chars + 'F', count + 1

    def puzzle_1(input_str):
        grid = []
        for line in open(input_str):
            grid.append(list(line.strip('\n')))
        return walk_grid(grid)[0]
    yield puzzle_1(puzzle_loc)

    def puzzle_2(input_str):
        grid = []
        for line in open(input_str):
            grid.append(list(line.strip('\n')))
        return walk_grid(grid)[1]
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_19 in day_19():
    print(solution_19)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

