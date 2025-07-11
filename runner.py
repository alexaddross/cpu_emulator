from core import SimpleCPU
from assembler import assemble
from utils import bytecode_splitter

cpu = SimpleCPU()

program_file = open('main.asm')
program_data = program_file.read()
program_file.close()

bytecode = assemble(
    program_data
)

for line in bytecode_splitter(bytecode):
    print(line)

cpu.load_program(bytecode)

cpu.run()

print(
    cpu.dump_state()
)