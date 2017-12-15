import re
from datetime import datetime
from collections import defaultdict


def day_8():
    regs_text = 'registers.txt'

    def pythonize_command(command, splitter=re.compile(r'(\w+) (\w+) (-?\d+) (\w+) (\w+) ([!<>=]+) (-?\d+)')):
        match = splitter.match(command)
        var_1 = 'registers["' + str(match.group(1)) + '"]'
        operator = 'inc' if match.group(2) == '+=' else '-='
        val_1 = match.group(3)
        if_ = match.group(4)
        var_2 = 'registers["' + str(match.group(5)) + '"]'
        condition = match.group(6)
        val_2 = match.group(7)
        return " ".join([if_, var_2, condition, val_2, ": ", var_1, operator, val_1])

    def puzzle_1(input_str):
        registers = defaultdict(int)
        for line in open(input_str):
            command = pythonize_command(line)
            exec(command)
        return max(registers.values())
    yield puzzle_1(regs_text)

    def puzzle_2(input_str):
        total_max = 0
        registers = defaultdict(int)
        for line in open(input_str):
            command = pythonize_command(line)
            exec(command)
            total_max = max(max(registers.values()), total_max)
        return total_max
    yield puzzle_2(regs_text)

now = datetime.now()
for solution_8 in day_8():
    print(solution_8)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

