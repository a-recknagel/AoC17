from datetime import datetime


def day_6():
    mem_loc = 'mem.txt'

    class MemBank:
        def __init__(self, initial_state):
            self.mem = [int(s) for s in initial_state.strip().split()]
            self.seen_states = dict()

        def re_allocate(self):
            str_mem = "".join([str(v) for v in self.mem])
            if str_mem in self.seen_states:
                return self.seen_states[str_mem]
            self.seen_states[str_mem] = len(self.seen_states)
            max_val = max(self.mem)
            max_idx = self.mem.index(max_val)
            self.mem[max_idx] = 0
            for idx in range(max_idx+1, max_idx+1+max_val):
                self.mem[idx % len(self.mem)] += 1
            return -1

    def puzzle_1(input_string):
        mem_instance = MemBank(" ".join(open(input_string).readlines()))
        while mem_instance.re_allocate() < 0:
            pass
        return len(mem_instance.seen_states)
    yield puzzle_1(mem_loc)

    def puzzle_2(input_string):
        mem_instance = MemBank(" ".join(open(input_string).readlines()))
        while True:
            first_seen = mem_instance.re_allocate()
            if first_seen >= 0:
                return len(mem_instance.seen_states) - first_seen
    yield puzzle_2(mem_loc)

now = datetime.now()
for solution_6 in day_6():
    print(solution_6)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
