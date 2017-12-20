from datetime import datetime


def day_20():
    puzzle_loc = 'particles.txt'

    def parse_input(file_loc):
        for line in open(file_loc):
            p, v, a = [val[3:-1] for val in line.strip().split(', ')]
            yield {
                'p': [int(val.strip()) for val in p.split(',')],
                'v': [int(val.strip()) for val in v.split(',')],
                'a': [int(val.strip()) for val in a.split(',')]
            }

    def small_comp(x, pos):
        return sum(abs(val) for val in x[1][pos])

    def puzzle_1(input_str):
        particles = [(idx, p) for idx, p in enumerate(list(parse_input(input_str)))]
        for comp in ['a', 'v', 'p']:
            smallest = sorted(particles, key=lambda x: small_comp(x, comp))[0]
            particles = [p for p in particles if small_comp(p, comp) == small_comp(smallest, comp)]
        return particles[0][0]
    yield puzzle_1(puzzle_loc)

    def puzzle_2(input_str):
        particles = list(parse_input(input_str))
        initial_length = len(particles)
        streak = 0
        while True:
            current_len = len(particles)
            to_delete = set()
            for idx_a in range(len(particles)):
                for idx_b in range(len(particles)):
                    if idx_a == idx_b:
                        continue
                    if particles[idx_a]['p'] == particles[idx_b]['p']:
                        to_delete.add(idx_a)
                        to_delete.add(idx_b)

            for particle in [particles[idx] for idx in to_delete]:
                particles.remove(particle)
            for particle in particles:
                particle['v'][0] += particle['a'][0]
                particle['v'][1] += particle['a'][1]
                particle['v'][2] += particle['a'][2]
                particle['p'][0] += particle['v'][0]
                particle['p'][1] += particle['v'][1]
                particle['p'][2] += particle['v'][2]
            if (initial_length * 0.9) > current_len and streak > 100:
                break
            if current_len == len(particles):
                streak += 1
            else:
                streak = 0
        return len(particles)
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_20 in day_20():
    print(solution_20)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
