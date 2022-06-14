'''Interprets release commands from an instruction block'''

# from github import Github

# from github_interpreter.argument_interpreter import retrieve_argument

# def create_release(github: Github, instruction) -> None:
#     '''Creates a release branch'''
#     repo_name = retrieve_argument(instruction, 'repo_name')
#     from_branch = retrieve_argument(instruction, 'from_branch')
#     to_branch = retrieve_argument(instruction, 'to_branch')
#     tag = retrieve_argument(instruction, 'tag')
#     release = retrieve_argument(instruction, 'release', is_required=False, default=None)
#     reviewers = retrieve_argument(instruction, 'reviewers', is_required=False, default=[])
#     labels = retrieve_argument(instruction, 'labels', is_required=False, default=[])
