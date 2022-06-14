'''Retrieves an argument from an instruction block'''
def retrieve_argument(instruction, argument: str, is_required: bool = True, default = None):
    '''Retrives an instruction argument - defaults to `default` if not required'''
    if not is_required:
        value = default
        if argument in instruction:
            value = instruction[argument]
        return value

    return instruction[argument]
