import sys

data = open(sys.argv[1]).readlines()
data = [x.split() for x in data]

class State:
    def __init__(
        self, 
        pc = 0,
        acc = 0,
        seen = set()
    ):
        self.pc = pc
        self.acc = acc
        self.seen = seen

    def copy(state):
        return State(state.pc, state.acc, state.seen.copy())
    

class Computer:
    def __init__(self):
        self.state = State()

    @classmethod
    def execute(cls, state, ins, value):
        new_state = state.copy()
        if (ins == 'nop'):
            pass
        elif (ins == 'acc'):
            new_state.acc += value
        elif (ins == 'jmp'):
            new_state.pc += value
            return new_state
        new_state.pc += 1
        return new_state


    def run(self, code):
        while True:
            if (self.state.pc in self.state.seen):
                return
            self.state.seen.add(self.state.pc)

            ins, value = code[self.state.pc]
            Computer.execute(ins, int(value))

    def run_predictive(self, code, state=State(), changed=False):
        if (state.pc in state.seen):
            return False
        state.seen.add(state.pc)

        if (state.pc >= len(code)):
            print("ACC",state.acc)
            import sys; sys.exit()

        ins, value = code[state.pc]
        value = int(value)

        if ((ins == 'nop' or ins == 'jmp') and not changed):
            new_state = Computer.execute(state, 'jmp' if ins == 'nop' else 'nop', value)
            self.run_predictive(code, new_state, True)

        new_state = Computer.execute(state, ins, value)
        return self.run_predictive(code, new_state, changed)

computer = Computer()
computer.run_predictive(data)
