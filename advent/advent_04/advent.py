from datetime import datetime


def day_4():
    pass_phrases = 'passphrases.txt'

    def puzzle_1(file_loc):
        valid_count = 0
        for line in open(file_loc):
            words = line.strip().split()
            if len(set(line.strip().split())) == len(words):
                valid_count += 1
        return valid_count
    yield puzzle_1(pass_phrases)

    def puzzle_2(file_loc):
        valid_count = 0
        for line in open(file_loc):
            frq_dists = []
            for word in line.strip().split():
                frq_dist = {}
                for c in word:
                    if c in frq_dist:
                        frq_dist[c] += 1
                    else:
                        frq_dist[c] = 1
                if frq_dist in frq_dists:
                    break
                else:
                    frq_dists.append(frq_dist)
            else:
                valid_count += 1
        return valid_count
    yield puzzle_2(pass_phrases)

now = datetime.now()
for solution_4 in day_4():
    print(solution_4)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

