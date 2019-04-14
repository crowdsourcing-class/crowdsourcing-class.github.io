import unittest
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files

class TestFiles(unittest.TestCase):
    @weight(0)
    def test_submitted_files(self):
        """Check submitted files: looking for 'homework7.py'"""
        missing_files = check_submitted_files(['homework7.py'])
        for path in missing_files:
            print('Missing %s' % path)
        self.assertEqual(len(missing_files), 0, 'Missing some required files!')
        print('All required files submitted!')
