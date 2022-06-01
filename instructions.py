'''Collection of supported instructions'''

class Instruction: # pylint: disable=too-few-public-methods
    '''Object describing a single instruction block'''
    action: str

class Instructions: # pylint: disable=too-few-public-methods
    '''Object describing a set of instructions'''
    name: str
    instructions: list[Instruction]
