import re
from datetime import datetime


def day_7():
    progs_text = 'programs.txt'

    class Prog:
        def __init__(self, name, weight):
            self.name = name
            self.weight = int(weight)
            self.total_weight = None
            self.children = []
            self.parent = None

    def build_tree(input_string,
                   splitter=re.compile(r'(\w+) \((\d+)\)( -> (.+))?')):
        progs = {}
        for line in open(input_string):
            match = splitter.match(line.strip())
            if match:
                progs[match.group(1)] = Prog(match.group(1), match.group(2)), match.group(4)
            else:
                print("false input read at '%s'" % line)

        for program, children in progs.values():
            if children:
                for child in children.split(", "):
                    program.children.append(progs[child][0])
                    progs[child][0].parent = program

        some_child = next(iter(progs.values()))[0]
        while some_child.parent:
            some_child = some_child.parent
        return some_child

    def puzzle_1(input_string):
        root = build_tree(input_string)
        return root.name
    yield puzzle_1(progs_text)

    def compute_total_weight(prog):
        total_weight = prog.weight
        for child in prog.children:
            total_weight += compute_total_weight(child)
        prog.total_weight = total_weight
        return prog.total_weight

    def find_deepest_inequal(prog):
        # test which child is in-equal
        child_dist = {}
        for child in prog.children:
            if child.total_weight in child_dist:
                child_dist[child.total_weight].append(child)
            else:
                child_dist[child.total_weight] = [child]
        if len(child_dist) > 1:
            # if one was found, note its correct weight and go deeper
            for weight, children in child_dist.items():
                if len(children) == 1:
                    unbalanced_child = children[0]
                else:
                    balanced_weight = weight
            # the most recently added child is the 'root' of the problem
            # noinspection PyUnboundLocalVariable
            find_deepest_inequal.solution = unbalanced_child.weight + (balanced_weight - unbalanced_child.total_weight)
            find_deepest_inequal(unbalanced_child)

    def puzzle_2(input_string):
        root = build_tree(input_string)
        compute_total_weight(root)
        find_deepest_inequal(root)
        # noinspection PyUnresolvedReferences
        return find_deepest_inequal.solution
    yield puzzle_2(progs_text)

now = datetime.now()
for solution_7 in day_7():
    print(solution_7)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
