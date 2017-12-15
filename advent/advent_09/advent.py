from datetime import datetime


def day_9():
    garb_text = 'garbage.txt'

    def skip_trash(content, idx):
        trash_size = 0
        while idx <= len(content):
            if content[idx] == '!':
                idx += 2
                continue
            if content[idx] == '>':
                return idx + 1, trash_size
            idx += 1
            trash_size += 1
        print("PARSE ERROR: Trash group not closed.")
        return idx, trash_size

    def parse(content, idx=0, depth=0):
        if idx == 0:
            parse.score = 0
            parse.trash = 0
        else:
            parse.score += depth
        while idx < len(content):
            current = content[idx]
            if current == '<':
                idx, trash_size = skip_trash(content, idx + 1)
                parse.trash += trash_size
                continue
            elif current == '{':
                idx = parse(content, idx + 1, depth + 1)
                continue
            elif current == '}':
                return idx + 1
            elif current == ',':
                pass  # is required between groups, but changes nothing.
            else:
                print("Parsing error at [%s, (%s), %s]" %
                      (' '.join(content[max(0, idx-3):idx]),
                       content[idx],
                       ', '.join(content[idx+1:min(len(content)-1, idx+4)])))
            idx += 1
        if depth != 0:
            print("Malformed input, not all brackets closed!")

    def puzzle_1(input_str):
        with open(input_str) as garbage_raw:
            all_input = garbage_raw.read().strip()
        parse(all_input)
        # noinspection PyUnresolvedReferences
        return parse.score
    yield puzzle_1(garb_text)

    def puzzle_2(input_str):
        with open(input_str) as garbage_raw:
            all_input = garbage_raw.read().strip()
        parse(all_input)
        # noinspection PyUnresolvedReferences
        return parse.trash
    yield puzzle_2(garb_text)

now = datetime.now()
for solution_9 in day_9():
    print(solution_9)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

