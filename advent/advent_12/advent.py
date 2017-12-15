from datetime import datetime


def day_12():
    pipes_text = 'pipes.txt'

    class Node:
        node_list = {}

        @staticmethod
        def connect_all():
            for node in Node.node_list.values():
                for child_id in node.children_ids:
                    node.edges.append(Node.node_list[child_id])

        def __init__(self, id_number, children_ids):
            self.id = int(id_number)
            Node.node_list[self.id] = self
            self.children_ids = map(int, children_ids)
            self.edges = []

    def parse_input(input_lines):
        for line in input_lines:
            node_id, children_ids = line.split('<->')
            node_id = node_id.strip()
            children_ids = [c_id.strip() for c_id in children_ids.split(',')]
            Node(node_id, children_ids)
        Node.connect_all()

    def traverse(current, accumulation):
        accumulation.add(current.id)
        for child in current.edges:
            if child.id not in accumulation:
                traverse(child, accumulation)
        return accumulation

    def puzzle_1(input_str):
        parse_input(open(input_str))
        connections = traverse(Node.node_list[0], set())
        return len(connections)
    yield puzzle_1(pipes_text)

    def puzzle_2(input_str):
        parse_input(open(input_str))
        groups = set()
        groups_union = set()
        for node in Node.node_list.values():
            if node.id in groups_union:
                continue
            connections = frozenset(traverse(node, set()))
            groups.add(connections)
            groups_union.update(connections)
        return len(groups)
    yield puzzle_2(pipes_text)

now = datetime.now()
for solution_12 in day_12():
    print(solution_12)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())
