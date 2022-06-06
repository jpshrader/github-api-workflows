'''Branch Management Tests'''
from unittest import TestCase

from github_functions.branch_management import branch_passes_filters

class StubBranch: # pylint: disable=too-few-public-methods
    '''Stub object for testing branch objects'''
    name: str

    def __init__(self, name: str):
        self.name = name

class BranchManagementTests(TestCase):
    '''Branch Management Test Fixture'''
    branch = StubBranch('main')
    include = [
        'main',
        'develop'
    ]
    exclude = [
        'master',
        'integration'
    ]

    def test_branch_management_exclude_branch(self) -> None:
        '''Verifies that `branch_passes_filters` excludes branches properly'''
        branch = StubBranch('master')
        result = branch_passes_filters(branch, [], self.exclude)

        self.assertFalse(result)

    def test_branch_management_include_branch(self) -> None:
        '''Verifies that `branch_passes_filters` excludes branches properly'''
        result = branch_passes_filters(self.branch, self.include, [])

        self.assertTrue(result)

    def test_branch_management_no_filters(self) -> None:
        '''Verifies that `branch_passes_filters` excludes branches properly'''
        result = branch_passes_filters(self.branch, [], [])

        self.assertTrue(result)

    def test_branch_management_overlapping_filters(self) -> None:
        '''Verifies that `branch_passes_filters` excludes branches properly when overlapping filters'''
        branch = StubBranch('master')
        include = [branch.name]
        exclude = [branch.name]
        result = branch_passes_filters(branch, include, exclude)

        self.assertFalse(result)
