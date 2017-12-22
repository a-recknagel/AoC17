from datetime import datetime


def day_22():
    puzzle_loc = 'map.txt'

    class Cell:
        cell_map = {}

        def __init__(self, x, y, infected=False):
            self.status = 'infected' if infected else 'clean'
            self.coord = x, y
            Cell.cell_map[self.coord] = self
            self.left = Cell.cell_map.get((x-1, y), None)
            if self.left is not None:
                self.left.right = self
            self.right = Cell.cell_map.get((x+1, y), None)
            if self.right is not None:
                self.right.left = self
            self.up = Cell.cell_map.get((x, y-1), None)
            if self.up is not None:
                self.up.down = self
            self.down = Cell.cell_map.get((x, y+1), None)
            if self.down is not None:
                self.down.up = self

        def go_left(self):
            if self.left is None:
                self.left = Cell(self.coord[0]-1, self.coord[1])
            return self.left

        def go_right(self):
            if self.right is None:
                self.right = Cell(self.coord[0]+1, self.coord[1])
            return self.right

        def go_up(self):
            if self.up is None:
                self.up = Cell(self.coord[0], self.coord[1]-1)
            return self.up

        def go_down(self):
            if self.down is None:
                self.down = Cell(self.coord[0], self.coord[1]+1)
            return self.down

        @staticmethod
        def print_cells():
            cells = list(Cell.cell_map.keys())
            min_x, max_x, min_y, max_y = (
                min(e[0] for e in cells),
                max(e[0] for e in cells),
                min(e[1] for e in cells),
                max(e[1] for e in cells),
            )
            for y in range(min_y, max_y+1):
                for x in range(min_x, max_x+1):
                    cell = Cell.cell_map.get((x, y), None)
                    if cell is None or cell.status == 'clean':
                        print('.', end='')
                    elif cell.status == 'weakened':
                        print('W', end='')
                    elif cell.status == 'flagged':
                        print('F', end='')
                    else:
                        print('#', end='')
                print()

    def parse_input(loc):
        Cell.cell_map = {}
        initial_infected_count = 0
        for y, line in enumerate(open(loc)):
            for x, c in enumerate(line.strip()):
                initial_infected_count += (c == '#')
                Cell(x, y, infected=(c == '#'))
        highest = sorted(Cell.cell_map.keys(), key=lambda e: e[0]+e[1])[-1]
        return initial_infected_count, Cell.cell_map[(highest[0]//2, highest[1]//2)]

    class Virus:
        def __init__(self, start_cell, start_dir):
            self.current = start_cell
            self.dir = start_dir
            self.infection_count = 0

        def work(self):
            if self.current.status == 'infected':
                self.turn_right()
                self.current.status = 'clean'
            else:  # self.current.status == 'clean'
                self.turn_left()
                self.current.status = 'infected'
                self.infection_count += 1
            self.step()

        def turn_right(self):
            if self.dir == 'left':
                self.dir = 'up'
            elif self.dir == 'up':
                self.dir = 'right'
            elif self.dir == 'right':
                self.dir = 'down'
            else:  # self.dir == 'down'
                self.dir = 'left'

        def turn_left(self):
            if self.dir == 'left':
                self.dir = 'down'
            elif self.dir == 'down':
                self.dir = 'right'
            elif self.dir == 'right':
                self.dir = 'up'
            else:  # self.dir == 'up'
                self.dir = 'left'

        def step(self):
            if self.dir == 'left':
                self.current = self.current.go_left()
            elif self.dir == 'right':
                self.current = self.current.go_right()
            elif self.dir == 'up':
                self.current = self.current.go_up()
            else:  # self.dir == 'down'
                self.current = self.current.go_down()

    def puzzle_1(input_str):
        initial_infected, current = parse_input(input_str)
        virus = Virus(current, 'up')
        for _ in range(0, 10000):
            virus.work()
        # Cell.print_cells()
        return virus.infection_count
    yield puzzle_1(puzzle_loc)

    class EvolvedVirus(Virus):
        def __init__(self, start_cell, start_dir):
            super().__init__(start_cell, start_dir)

        def turn_around(self):
            if self.dir == 'left':
                self.dir = 'right'
            elif self.dir == 'right':
                self.dir = 'left'
            elif self.dir == 'up':
                self.dir = 'down'
            else:  # self.dir == 'down'
                self.dir = 'up'

        def work(self):
            if self.current.status == 'clean':
                self.turn_left()
                self.current.status = 'weakened'
            elif self.current.status == 'weakened':
                self.current.status = 'infected'
                self.infection_count += 1
            elif self.current.status == 'infected':
                self.turn_right()
                self.current.status = 'flagged'
            else:  # self.current.status == 'flagged'
                self.turn_around()
                self.current.status = 'clean'
            self.step()

    def puzzle_2(input_str):
        initial_infected, current = parse_input(input_str)
        virus = EvolvedVirus(current, 'up')
        for _ in range(0, 10000000):
            virus.work()
        # Cell.print_cells()
        return virus.infection_count
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_22 in day_22():
    print(solution_22)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
