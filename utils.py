from numpy import array_split


def bytecode_splitter(bytecode: list):
    return array_split(bytecode, len(bytecode) // 3)