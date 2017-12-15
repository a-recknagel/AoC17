from datetime import datetime


def day_5():
    file_location = 'jumps.txt'

    def jump_1(instr_list):
        counter = 0
        current = 0
        while True:
            try:
                instr_list[current] += 1
            except IndexError:
                return counter
            counter += 1
            current += (instr_list[current] - 1)

    def puzzle_1(input_location):
        with open(input_location) as jumps_raw:
            return jump_1([int(line) for line in jumps_raw])
    yield puzzle_1(file_location)

    def jump_2(instr_list):
        counter = 0
        current = 0
        while True:
            try:
                offset = instr_list[current]
            except IndexError:
                return counter
            if instr_list[current] > 2:
                instr_list[current] -= 1
            else:
                instr_list[current] += 1
            counter += 1
            current += offset

    def puzzle_2(input_location):
        with open(input_location) as jumps_raw:
            return jump_2([int(line) for line in jumps_raw])
    yield puzzle_2(file_location)

now = datetime.now()
for solution_5 in day_5():
    print(solution_5)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

