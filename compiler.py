from argparse import ArgumentParser
from assembler import assemble

parser = ArgumentParser()
parser.add_argument('filename', required=True)

# TODO: Write some tool for compiling the assembler instructions for the virtual CPU
