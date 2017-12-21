from datetime import datetime


def day_21():
    puzzle_loc = 'rules.txt'

    def rotate(pattern):
        if len(pattern) == 2:
            ret = [pattern[1][0] + pattern[0][0],
                   pattern[1][1] + pattern[0][1]]
        else:  # len(pattern) == 3
            ret = [pattern[2][0] + pattern[1][0] + pattern[0][0],
                   pattern[2][1] + pattern[1][1] + pattern[0][1],
                   pattern[2][2] + pattern[1][2] + pattern[0][2]]
        return tuple(ret)

    def flip(pattern):
        ret = []
        l = len(pattern)
        for idx in range(l):
            ret.append(pattern[idx][::-1])
        return tuple(ret)

    def blockify(grid):
        def inner(div):
            ret = []
            for idx_1 in range(len(grid) // div):
                ret.append([])
                for idx_2 in range(len(grid) // div):
                    block = [grid[idx_1*div+i][idx_2*div:idx_2*div+div] for i in range(div)]
                    ret[-1].append(block)
            return ret
        if len(grid) % 2 == 0:
            return inner(2)
        else:
            return inner(3)

    def de_blockify(blocks):
        ret = []
        for block_row in blocks:
            for row in range(len(block_row[0])):
                ret.append('')
                for outer_col in range(len(block_row)):
                    for inner_col in range(len(block_row[0])):
                        ret[-1] += block_row[outer_col][row][inner_col]
        return ret

    def expand_rules(rule_loc):
        ret = {}
        count = 0
        for line in open(rule_loc):
            count += 1
            input_str, output_str = line.strip().split(' => ')
            in_grid = tuple([val for val in input_str.split('/')])
            out_grid = tuple([val for val in output_str.split('/')])
            for _ in range(4):
                ret[in_grid] = out_grid
                ret[flip(in_grid)] = out_grid
                in_grid = rotate(in_grid)
        return ret

    def puzzle_1(input_str):
        rules = expand_rules(input_str)
        current = ['.#.', '..#', '###']
        for iteration in range(1, 6):
            blocks = blockify(current)
            for idx_1 in range(len(blocks)):
                for idx_2 in range(len(blocks[idx_1])):
                    blocks[idx_1][idx_2] = rules[tuple(blocks[idx_1][idx_2])]
            current = de_blockify(blocks)
        return sum([row.count('#') for row in current])
    yield puzzle_1(puzzle_loc)

    def puzzle_2(input_str):
        rules = expand_rules(input_str)
        current = ['.#.', '..#', '###']
        for iteration in range(1, 19):
            blocks = blockify(current)
            for idx_1 in range(len(blocks)):
                for idx_2 in range(len(blocks[idx_1])):
                    blocks[idx_1][idx_2] = rules[tuple(blocks[idx_1][idx_2])]
            current = de_blockify(blocks)
        return sum([row.count('#') for row in current])
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_21 in day_21():
    print(solution_21)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
