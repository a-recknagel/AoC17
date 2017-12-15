from datetime import datetime


def day_11():
    hex_text = 'hexes.txt'

    class Coord:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __add__(self, other):
            return Coord(self.x + other.x, self.y + other.y, self.z + other.z)

    step_to_coord = {
        'n': Coord(1, 0, -1),
        'ne': Coord(1, -1, 0),
        'nw': Coord(0, 1, -1),
        's': Coord(-1, 0, 1),
        'se': Coord(0, -1, 1),
        'sw': Coord(-1, 1, 0),
    }

    def puzzle_1(input_str):
        with open(input_str) as steps_raw:
            all_steps = steps_raw.read().strip().split(',')
        current = Coord(0, 0, 0)
        for step in all_steps:
            current += step_to_coord[step]
        return max(abs(current.x), abs(current.y), abs(current.z))
    yield puzzle_1(hex_text)

    def puzzle_2(input_str):
        with open(input_str) as steps_raw:
            all_steps = steps_raw.read().strip().split(',')
        greatest_dist = 0
        current = Coord(0, 0, 0)
        for step in all_steps:
            current += step_to_coord[step]
            greatest_dist = max(greatest_dist, max(abs(current.x), abs(current.y), abs(current.z)))
        return greatest_dist
    yield puzzle_2(hex_text)

now = datetime.now()
for solution_11 in day_11():
    print(solution_11)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

