
def advent_17():

    class Link:
        length = 0
        root = None

        def __init__(self, val, before_link=None):
            if before_link is None:
                before_link = self
                self.next_link = self
                Link.root = self
            self.val = val
            self.next_link = before_link.next_link
            before_link.next_link = self
            Link.length += 1

        def __str__(self):
            current = Link.root
            ret = '['
            for _ in range(Link.length):
                if current == self:
                    ret += '(' + str(current.val) + '), '
                else:
                    ret += str(current.val) + ', '
                current = current.next_link
            return ret[:-2] + ']'

    def puzzle_1(step_nr):
        current = Link(0)
        for counter in range(1, 2018):
            for _ in range(step_nr % Link.length):
                current = current.next_link
            current = Link(counter, current)
        return current.next_link.val
    yield puzzle_1(363)

    def puzzle_2(step_nr):
        current = 0
        ret = 1
        for idx in range(1, 50000001):
            current = ((current + step_nr) % idx) + 1
            if current == 1:
                ret = idx
        return ret
    yield puzzle_2(363)

for answer in advent_17():
    print(answer)
