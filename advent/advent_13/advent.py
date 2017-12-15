from itertools import count
from datetime import datetime


def day_13():
    pipes_loc = 'layers.txt'

    class Field:
        def __init__(self, layers):
            layers_raw = [line.strip().split(': ') for line in open(layers)]
            layers_pairs = {int(depth): int(range_) for depth, range_ in layers_raw}
            self.layers = []
            for idx in range(int(layers_raw[-1][0])+1):
                if idx in layers_pairs:
                    self.layers.append([0, layers_pairs[idx]])
                else:
                    self.layers.append(None)
            self.pass_generators = []
            for depth, layer in enumerate(self.layers):
                if not layer:
                    continue
                self.pass_generators.append([Field.skip_func(depth, layer[1])])
                self.pass_generators[-1].append(next(self.pass_generators[-1][0]))

        @staticmethod
        def skip_func(depth, range_):
            return (pass_idx for pass_idx in count() if
                    ((pass_idx+depth) % (range_*2-2)) != 0)

        def test_wait_time(self, wait):
            for _, pair in enumerate(self.pass_generators):
                while pair[1] < wait:
                    pair[1] = next(pair[0])
                if pair[1] != wait:
                    return False
            else:
                return True

        def update(self):
            for layer in self.layers:
                if not layer:
                    continue
                layer[0] = (layer[0]+1) % (layer[1] * 2 - 2)

        def reset(self):
            for layer in self.layers:
                if layer:
                    layer[0] = 0

    def puzzle_1(input_str):
        field = Field(input_str)
        score = 0
        for current, layer in enumerate(field.layers):
            if layer and layer[0] == 0:
                score += current * layer[1]
            field.update()
        return int(round(score))
    yield puzzle_1(pipes_loc)

    def puzzle_2(input_str):
        field = Field(input_str)
        for wait_time in count():
            if field.test_wait_time(wait_time):
                return wait_time
    yield puzzle_2(pipes_loc)

now = datetime.now()
for solution_13 in day_13():
    print(solution_13)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

