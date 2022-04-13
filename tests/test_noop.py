from unittest import TestCase

class noop(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)