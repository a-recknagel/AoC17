from datetime import datetime
from collections import defaultdict


def day_18():
    puzzle_loc = 'registers.txt'

    class Register:
        def __init__(self):
            self.current = 0
            self.last_sound = None
            self.registers = defaultdict(int)
            self.dispatcher = {
                'snd': self.snd,
                'set': self.set,
                'add': self.add,
                'mul': self.mul,
                'mod': self.mod,
                'rcv': self.rcv,
                'jgz': self.jgz,
            }

        def untangle(self, v):
            try:
                return int(v)
            except ValueError:
                return self.registers[v]

        def snd(self, v):
            self.last_sound = self.untangle(v)

        def set(self, r, v):
            self.registers[r] = self.untangle(v)

        def add(self, r, v):
            self.registers[r] += self.untangle(v)

        def mul(self, r, v):
            self.registers[r] *= self.untangle(v)

        def mod(self, r, v):
            self.registers[r] %= self.untangle(v)

        def rcv(self, v):
            return self.last_sound if self.untangle(v) != 0 else None

        def jgz(self, v_1, v_2):
            self.current += (self.untangle(v_2) - 1) if self.untangle(v_1) > 0 else 0

        def __call__(self, arg_list):
            return self.dispatcher[arg_list[0]](*arg_list[1:])

    def puzzle_1(input_str):
        instruction_list = [line.strip().split(' ') for line in open(input_str)]
        reg = Register()
        while 0 <= reg.current < len(instruction_list):
            command = instruction_list[reg.current]
            ret = reg(command)
            if ret is not None:
                return ret
            reg.current += 1
    yield puzzle_1(puzzle_loc)

    class DuetRegister(Register):
        call_stack = {}

        def __init__(self, p_id, target_id):
            super().__init__()
            self.p_id = p_id
            self.registers['p'] = self.p_id
            DuetRegister.call_stack[self.p_id] = []
            self.target = target_id
            self.send_count = 0
            self.locked = False
            self.dispatcher['snd'] = self.snd
            self.dispatcher['rcv'] = self.rcv

        def snd(self, v):
            DuetRegister.call_stack[self.target].append(self.untangle(v))
            self.send_count += 1

        def rcv(self, r):
            if DuetRegister.call_stack[self.p_id]:
                self.registers[r] = self.untangle(DuetRegister.call_stack[self.p_id][0])
                DuetRegister.call_stack[self.p_id] = DuetRegister.call_stack[self.p_id][1:]
                self.locked = False
            else:
                self.locked = True
                self.current -= 1  # busy wait

    def puzzle_2(input_str):
        instruction_list = [line.strip().split(' ') for line in open(input_str)]
        reg_0 = DuetRegister(0, 1)
        reg_1 = DuetRegister(1, 0)
        while (0 <= reg_0.current < len(instruction_list) and
               0 <= reg_1.current < len(instruction_list) and not
                (reg_0.locked and reg_1.locked)):
            reg_0(instruction_list[reg_0.current])
            reg_1(instruction_list[reg_1.current])
            reg_0.current += 1
            reg_1.current += 1
        return reg_1.send_count
    yield puzzle_2(puzzle_loc)

now = datetime.now()
for solution_18 in day_18():
    print(solution_18)
    pass
print("Took a total of %.3f seconds\n" % (datetime.now() - now).total_seconds())

