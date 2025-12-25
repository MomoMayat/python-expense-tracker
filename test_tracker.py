import os
import csv
import unittest
from tracker import add_expense

class TestTracker(unittest.TestCase):
    def test_add_expense(self):
        """Verify that we can add an expense to the CSV file correctly."""
        test_file = 'debug_test.csv'

        # Clean old test files
        if os.path.exists(test_file):
            os.remove(test_file)

        add_expense(15.75, "Lunch", filename=test_file)

        # read file to verify results
        with open(test_file, 'r') as f:
            reader = list(csv.reader(f))
            # index 0 is headers, index 1 is the data
            self.assertEqual(reader[1][0], '15.75')
            self.assertEqual(reader[1][1], 'Lunch')

        # clean up test file
        os.remove(test_file)

if __name__ == '__main__':
    unittest.main()