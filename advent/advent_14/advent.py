from itertools import count
from datetime import datetime


def day_14():

    def asciify(input_string):
        return [ord(c) for c in input_string] + [17, 31, 73, 47, 23]

    def encrypt(input_list, hashes, current, skip_size):
        input_copy = list(input_list)
        for length in (length for length in hashes if length <= len(input_copy)):
            for idx in (range(length // 2)):
                idx_1 = (current + idx) % len(input_copy)
                idx_2 = ((current + (length - 1)) - idx) % len(input_copy)
                swap = input_copy[idx_1]
                input_copy[idx_1] = input_copy[idx_2]
                input_copy[idx_2] = swap
            current += (length + skip_size)
            current %= len(input_copy)
            skip_size += 1
        return input_copy, current, skip_size

    def densify(sparse_hash):
        dense_hash = []
        for block in [sparse_hash[i*16:i*16+16] for i in range(16)]:
            dense_hash.append(0)
            for val in block:
                dense_hash[-1] ^= val
        hexify = [hex(val)[2:] for val in dense_hash]
        return ''.join([val if len(val) == 2 else '0'+val for val in hexify])

    def get_mem_representation(raw_input):
        for row in range(128):
            current = 0
            skip_size = 0
            knot_hash_sparse = range(256)
            asciified_input = asciify(raw_input + '-' + str(row))
            for _ in range(64):
                knot_hash_sparse, current, skip_size = encrypt(
                    knot_hash_sparse, asciified_input, current, skip_size)
            knot_hash = densify(knot_hash_sparse)
            yield bin(int(knot_hash, 16))[2:].zfill(128)

    def puzzle_1(raw_input):
        mem = get_mem_representation(raw_input)
        return sum([line.count('1') for line in mem])
    yield puzzle_1('ljoxqyyw')

    def puzzle_2(raw_input):
        next_int = count(1)
        mem = list(get_mem_representation(raw_input))
        groups = [[0]*len(mem[0]) for _ in range(len(mem))]

        def explore(i, j, group_idx=0):
            if groups[i][j] or mem[i][j] == '0':
                return
            if group_idx == 0:
                group_idx = next(next_int)
            groups[i][j] = group_idx
            if (i-1) >= 0:
                explore(i-1, j, group_idx)
            if (i+1) < len(mem):
                explore(i+1, j, group_idx)
            if (j-1) >= 0:
                explore(i, j-1, group_idx)
            if (j+1) < len(mem[0]):
                explore(i, j+1, group_idx)

        for test_row in range(len(mem)):
            for test_col in range(len(mem[0])):
                explore(test_row, test_col)
        return max([max(row) for row in groups])
    yield puzzle_2('ljoxqyyw')

now = datetime.now()
for solution_14 in day_14():
    print(solution_14)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
