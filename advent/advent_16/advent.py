from datetime import datetime


def day_16():
    puzzle_loc = 'moves.txt'

    def dance(dancers, moves):
        tmp_list = list(dancers)
        l = len(tmp_list)
        for move in moves:
            if move.startswith('s'):
                dist = int(move[1:]) % l
                tmp_list = tmp_list[l - dist:] + tmp_list[:l - dist]
            elif move.startswith('x'):
                swap = [int(x) for x in move[1:].split('/')]
                tmp = tmp_list[swap[0]]
                tmp_list[swap[0]] = tmp_list[swap[1]]
                tmp_list[swap[1]] = tmp
            else:  # move.startswith('p')
                swap = [tmp_list.index(p) for p in move[1:].split('/')]
                tmp = tmp_list[swap[0]]
                tmp_list[swap[0]] = tmp_list[swap[1]]
                tmp_list[swap[1]] = tmp
        return tmp_list

    def puzzle_1(input_str):
        dancers = [c for c in 'abcdefghijklmnop']
        moves = open(input_str).read().split(',')
        dancers = dance(dancers, moves)
        return ''.join(dancers)
    yield puzzle_1(puzzle_loc)

    def first_rep(dancers, moves):
        current = tuple(dancers)
        states = set()
        while current not in states:
            states.add(current)
            current = tuple(dance(current, moves))
        return len(states)

    def puzzle_2(input_str):
        dancers = [c for c in 'abcdefghijklmnop']
        moves = open(input_str).read().split(',')
        for _ in range(1000000000 % first_rep(dancers, moves)):
            dancers = dance(dancers, moves)
        return ''.join(dancers)

    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_16 in day_16():
    print(solution_16)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
