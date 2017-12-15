from datetime import datetime
from itertools import islice


def day_15():

    def number_gen(current, mult):
        while True:
            current *= mult
            current %= 2147483647
            bin_rep = bin(current)[2:]
            yield bin_rep[len(bin_rep)-16:].zfill(16)

    def number_gen_mod(current, mult, mod):
        while True:
            current *= mult
            current %= 2147483647
            if current % mod == 0:
                bin_rep = bin(current)[2:]
                yield bin_rep[len(bin_rep)-16:].zfill(16)

    def puzzle_1(start_a, start_b):
        counter = 0
        generators = zip(number_gen(start_a, 16807), number_gen(start_b, 48271))
        for num_a, num_b in islice(generators, 0, 40000000):
            counter += int(num_a == num_b)
        return counter
    yield puzzle_1(634, 301)

    def puzzle_2(start_a, start_b):
        counter = 0
        generators = zip(number_gen_mod(start_a, 16807, 4), number_gen_mod(start_b, 48271, 8))
        for num_a, num_b in islice(generators, 0, 5000000):
            counter += int(num_a == num_b)
        return counter
    yield puzzle_2(634, 301)

now = datetime.now()
for solution_15 in day_15():
    print(solution_15)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

