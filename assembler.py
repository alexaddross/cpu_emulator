INSTRUCTION_MAP = {
    'MOV': 0x01,
    'ADD': 0x02,
    'SUB': 0x03,
    'JMP': 0x04,
    'PUSH': 0x05,
    'CALL': 0x06,
    'RET': 0x07,
    'HLT': 0xFF,
}

REGISTERS = {
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
}

def assemble(asm_code: str):
    bytecode = []
    lines = asm_code.strip().splitlines()
    for line in lines:
        line = line.split(';')[0].strip()
        if not line:
            continue
        parts = line.replace(',', '').split()
        instr = parts[0].upper()
        opcode = INSTRUCTION_MAP[instr]

        if instr == 'RET' or instr == 'HLT':
            bytecode += [opcode, 0, 0]
        elif instr == 'PUSH':
            reg = REGISTERS[parts[1].upper()]
            bytecode += [opcode, reg, 0]
        elif instr == 'JMP' or instr == 'CALL':
            addr = int(parts[1], 0)
            bytecode += [opcode, addr, 0]
        elif instr == 'MOV':
            reg = REGISTERS[parts[1].upper()]
            imm = int(parts[2], 0)
            bytecode += [opcode, reg, imm]
        elif instr == 'ADD' or instr == 'SUB':
            r1 = REGISTERS[parts[1].upper()]
            r2 = REGISTERS[parts[2].upper()]
            bytecode += [opcode, r1, r2]

    return bytecode
