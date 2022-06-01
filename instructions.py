'''Collection of supported instructions'''
MERGE_BRANCH = 'merge_branch'

def is_valid_instruction(instruction_name: str) -> bool:
    '''Determines whether the given instruction name is supported'''
    valid_instructions = [MERGE_BRANCH]

    return instruction_name in valid_instructions
