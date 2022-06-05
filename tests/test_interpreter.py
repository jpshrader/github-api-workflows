'''Interpreter Tests'''
from unittest import TestCase

from interpreter import retrieve_argument

class InterpretorTests(TestCase):
    '''Placeholder Test Fixture'''
    instruction = {
        'value_string': '123',
        'value_int': 123
    }

    def test_retrieve_argument_default_string(self) -> None:
        '''Verifies that `retrieve_argument` default strings correctly'''
        result = retrieve_argument(self.instruction, 'not_found', is_required=False, default='')
        self.assertEqual(result, '')

    def test_retrieve_argument_default_int(self) -> None:
        '''Verifies that `retrieve_argument` default ints correctly'''
        result = retrieve_argument(self.instruction, 'not_found', is_required=False, default=0)
        self.assertEqual(result, 0)

    def test_retrieve_argument_default_object(self) -> None:
        '''Verifies that `retrieve_argument` default objects correctly'''
        result = retrieve_argument(self.instruction, 'not_found', is_required=False, default={})
        self.assertEqual(result, {})

    def test_retrieve_argument_default_array(self) -> None:
        '''Verifies that `retrieve_argument` default arrays correctly'''
        result = retrieve_argument(self.instruction, 'not_found', is_required=False, default=[])
        self.assertEqual(result, [])

    def test_retrieve_argument_returns_error_when_is_required_not_found(self) -> None:
        '''Verifies that `retrieve_argument` throws an error when `is_required` is true and argument not found'''
        try:
            retrieve_argument(self.instruction, 'not_found', is_required=True)
        except KeyError as exc:
            self.assertIsNotNone(exc)

    def test_retrieve_argument_is_required_returns_string(self) -> None:
        '''Verifies that `retrieve_argument` returns the proper string value when `is_required` is true'''
        result = retrieve_argument(self.instruction, 'value_string', is_required=True)
        self.assertEqual(result, '123')

    def test_retrieve_argument_is_required_returns_int(self) -> None:
        '''Verifies that `retrieve_argument` returns the proper int value when `is_required` is true'''
        result = retrieve_argument(self.instruction, 'value_int', is_required=True)
        self.assertEqual(result, 123)

    def test_retrieve_argument_returns_string(self) -> None:
        '''Verifies that `retrieve_argument` returns the proper string value when `is_required` is false'''
        result = retrieve_argument(self.instruction, 'value_string', is_required=True)
        self.assertEqual(result, '123')

    def test_retrieve_argument_returns_int(self) -> None:
        '''Verifies that `retrieve_argument` returns the proper int value when `is_required` is false'''
        result = retrieve_argument(self.instruction, 'value_int', is_required=True)
        self.assertEqual(result, 123)
