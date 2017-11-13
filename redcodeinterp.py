
class Instruction:
    def __init__(self):
        pass

class Program:
    instructions = []

    def __init__(self):
        pass

    def add(ins: Instruction):
        self.instructions.append(ins)

class Mov:
    def __init__(self, dest, src):
        self.dest = dest
        self.src = src

    def __str__(self):
        return "MOV " + self.dest + ", " + self.src

class Add:
    def __init__(self, dest, src):
        self.dest = dest
        self.src = src

    def __src__(self):
        return "ADD " + self.dest + ", " + self.src

class Nop:
    def __init__(self):
        pass

    def __str__(self):
        return "NOP"
