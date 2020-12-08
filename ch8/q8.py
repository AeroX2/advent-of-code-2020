import sys

data = open(sys.argv[1]).readlines()
data = [x.split() for x in data]

class Computer:
    def __init__(self):
        self.pc = 0
        self.acc = 0
        self.seen = set()

    def execute(self, ins, value):
        if (ins == 'nop'):
            pass    
        elif (ins == 'acc'):
            self.acc += value
        elif (ins == 'jmp'):
            self.pc += value
            return
        self.pc += 1


    def run(self, code):
        while True:
            if (self.pc in self.seen):
                print("ACC:", self.acc)
                return
            self.seen.add(self.pc)

            ins, value = code[self.pc]
            self.execute(ins, int(value))

computer = Computer()
try:
    computer.run(data)
except:
    print(computer.acc)
