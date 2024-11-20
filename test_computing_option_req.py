import unittest
from computing_option import ComputingOption, Course

class TestComputingOption(unittest.TestCase):

    def setUp(self):
        self.computing_option = ComputingOption()

    def test_meets_all_requirements(self):
        courses = [
            {"discipline": "CS", "code": "115"},  # From List 1
            {"discipline": "CS", "code": "136"},  # From List 2
            {"discipline": "ECE", "code": "457A"},  # From List 3
            {"discipline": "CS", "code": "446"},  # From List 3
            {"discipline": "SYDE", "code": "223"},  # Additional
            {"discipline": "CHE", "code": "120"},  # Additional
        ]
        result = self.computing_option.check_requirements(courses)
        self.assertTrue(result)

    def test_missing_list_1(self):
        courses = [
            {"discipline": "CS", "code": "136"},  # From List 2
            {"discipline": "ECE", "code": "457"},  # From List 3
            {"discipline": "CS", "code": "231"},  # From List 3
            {"discipline": "SYDE", "code": "223"},  # Additional
            {"discipline": "CHE", "code": "120"},  # Additional
        ]
        result = self.computing_option.check_requirements(courses)
        self.assertFalse(result)

    def test_missing_list_2(self):
        courses = [
            {"discipline": "CS", "code": "115"},  # From List 1
            {"discipline": "ECE", "code": "457"},  # From List 3
            {"discipline": "CS", "code": "231"},  # From List 3
            {"discipline": "SYDE", "code": "223"},  # Additional
            {"discipline": "CHE", "code": "120"},  # Additional
        ]
        result = self.computing_option.check_requirements(courses)
        self.assertFalse(result)

    def test_missing_list_3(self):
        courses = [
            {"discipline": "CS", "code": "115"},  # From List 1
            {"discipline": "CS", "code": "136"},  # From List 2
            {"discipline": "SYDE", "code": "223"},  # Additional
            {"discipline": "CHE", "code": "120"},  # Additional
        ]
        result = self.computing_option.check_requirements(courses)
        self.assertFalse(result)

    def test_missing_additional_courses(self):
        courses = [
            {"discipline": "CS", "code": "115"},  # From List 1
            {"discipline": "CS", "code": "136"},  # From List 2
            {"discipline": "ECE", "code": "457"},  # From List 3
            {"discipline": "CS", "code": "231"},  # From List 3
        ]
        result = self.computing_option.check_requirements(courses)
        self.assertFalse(result)

    def test_missing_elective_requirements(self):
        courses = [
            {"discipline": "CS", "code": "115"},  # From List 1
            {"discipline": "CS", "code": "136"},  # From List 2
            {"discipline": "ECE", "code": "457"},  # From List 3
            {"discipline": "CS", "code": "231"},  # From List 3
            {"discipline": "SYDE", "code": "223"},  # Additional (not elective)
            {"discipline": "SYDE", "code": "121"},  # Additional (not elective)
        ]
        result = self.computing_option.check_requirements(courses)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
