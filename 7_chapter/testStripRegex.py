import unittest
from stripRegex import stripRegex


class TestStripRegex(unittest.TestCase):

    def test_stripRegex(self):
        self.assertEqual(stripRegex('   time  '), 'time')
        self.assertEqual(stripRegex('  time'), 'time')
        self.assertEqual(stripRegex('time'), 'time')
        self.assertEqual(stripRegex('--time--'), '--time--')
        self.assertEqual(stripRegex('--time--', '-'), 'time')
        self.assertEqual(stripRegex('**time', '*'), 'time')

if __name__ == '__main__':
    unittest.main()
