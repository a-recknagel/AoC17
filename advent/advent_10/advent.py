from datetime import datetime


def day_10():
    hash_text = 'hash.txt'

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

    def puzzle_1(input_str):
        with open(input_str) as hashes_raw:
            hashes = hashes_raw.read().strip().split(',')
        result = encrypt(range(256), (int(hash_str) for hash_str in hashes), 0, 0)[0]
        return result[0] * result[1]
    yield puzzle_1(hash_text)

    def densify(sparse_hash):
        dense_hash = []
        for block in [sparse_hash[i*16:i*16+16] for i in range(16)]:
            dense_hash.append(0)
            for val in block:
                dense_hash[-1] ^= val
        hexify = [hex(val)[2:] for val in dense_hash]
        return ''.join([val if len(val) == 2 else '0'+val for val in hexify])

    def asciify(input_string):
        return [ord(c) for c in input_string] + [17, 31, 73, 47, 23]

    def puzzle_2(input_str):
        with open(input_str) as hashes_raw:
            hashes = asciify(hashes_raw.read().strip())
        sparse_hash = range(256)
        current = 0
        skip_size = 0
        for _ in range(64):
            sparse_hash, current, skip_size = encrypt(
                sparse_hash, hashes, current, skip_size)
        dense_hash = densify(sparse_hash)
        return dense_hash

    yield puzzle_2(hash_text)

now = datetime.now()
for solution_10 in day_10():
    print(solution_10)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
