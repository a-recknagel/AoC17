from datetime import datetime


def day_3():
    def next_dir():
        current = ('x', 1)
        while True:
            yield current
            if current == ('x', 1):
                current = ('y', 1)
            elif current == ('y', 1):
                current = ('x', -1)
            elif current == ('x', -1):
                current = ('y', -1)
            else:  # current == ('y', -1)
                current = ('x', 1)

    def change_dir():
        countdown = 0
        grow = 0.0
        while True:
            if int(round(countdown)) == 0:
                grow += 0.5
                countdown = grow
                yield True
            else:
                countdown -= 1
                yield False

    def puzzle_1(x):
        x -= 1  # this array begins at 1, even if my computation doesn't
        directions = next_dir()
        dir_counts = dict.fromkeys('xy', 0)
        direction, step = next(directions)
        for _, change in zip(range(x), change_dir()):
            dir_counts[direction] += step
            if change:
                direction, step = next(directions)
        return abs(dir_counts['x']) + abs(dir_counts['y'])
    yield puzzle_1(265149)

    def get_sum(array, position):
        return (array[position[0] - 1][position[1] - 1] +
                array[position[0] + 0][position[1] - 1] +
                array[position[0] + 1][position[1] - 1] +
                array[position[0] - 1][position[1] + 0] +
                array[position[0] + 0][position[1] + 0] +  # always 0
                array[position[0] + 1][position[1] + 0] +
                array[position[0] - 1][position[1] + 1] +
                array[position[0] + 0][position[1] + 1] +
                array[position[0] + 1][position[1] + 1])

    def next_pos(current, direction, step):
        if direction == 'x':
            return current[0], current[1] + step
        if direction == 'y':
            return current[0] + step, current[1]

    def puzzle_2(y, size=100):
        directions = next_dir()
        mem = [[0]*size for _ in range(size)]
        current_pos = (size//2, size//2)
        mem[current_pos[0]][current_pos[1]] = 1
        direction, step = next(directions)
        for _, change in zip(range(2, size * size), change_dir()):
            current_pos = next_pos(current_pos, direction, step)
            current_sum = get_sum(mem, current_pos)
            if current_sum > y:
                return current_sum
            mem[current_pos[0]][current_pos[1]] = current_sum
            if change:
                direction, step = next(directions)
        print("Iteration ended, please pick a bigger 'size' parameter")
        return None
    yield puzzle_2(265149)

now = datetime.now()
for solution_3 in day_3():
    print(solution_3)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())