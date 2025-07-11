class SimpleCPU:
    def __init__(self, memory_size=256):
        self.memory = [0] * memory_size
        self.registers = [0] * 4  # R0-R3
        self.PC = 0
        self.SP = memory_size  # Stack Pointer (grows down)
        self.running = True

        self.OPCODES = {
            0x01: self.op_mov,
            0x02: self.op_add,
            0x03: self.op_sub,
            0x04: self.op_jmp,
            0x05: self.op_push,
            0x06: self.op_call,
            0x07: self.op_ret,
            0xFF: self.op_hlt,
        }

    def load_program(self, program_bytes):
        self.memory[:len(program_bytes)] = program_bytes

    def run(self):
        while self.running:
            opcode = self.memory[self.PC]
            op1 = self.memory[self.PC + 1]
            op2 = self.memory[self.PC + 2]
            self.PC += 3
            self.OPCODES.get(opcode, self.op_unknown)(op1, op2)

    def op_unknown(self, *args):
        raise Exception(f"Unknown opcode at {self.PC - 3}")

    def op_mov(self, reg, value):
        self.registers[reg] = value

    def op_add(self, r1, r2):
        self.registers[r1] += self.registers[r2]

    def op_sub(self, r1, r2):
        self.registers[r1] -= self.registers[r2]

    def op_jmp(self, addr, _):
        self.PC = addr

    def op_push(self, reg, _):
        self.SP -= 1
        self.memory[self.SP] = self.registers[reg]

    def op_call(self, addr, _):
        self.SP -= 1
        self.memory[self.SP] = self.PC
        self.PC = addr

    def op_ret(self, *_):
        self.PC = self.memory[self.SP]
        self.SP += 1

    def op_hlt(self, *_):
        self.running = False

    def dump_state(self):
        print("Registers:", self.registers)
        print("PC:", self.PC, "SP:", self.SP)
