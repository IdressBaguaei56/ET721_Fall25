"""
Idress Baguaei 
Oct 15, 2025 
Lab 9 file operations test 
"""
import unittest
import os 
from file_operations import read_file, write_file, append_file

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test
        self.filename = "test_file.txt"
        self.msg = "Idress Baguaei"

    def tearDown(self):
        # remove the test file after each test 
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        # test writing text to a file 
        msg = "Idress Baguaei"
        with open(self.filename, "w ")  as f:
            f.write(msg)

            # verify file exits and content matches 
            self.assertTrue(os.path.exits(self.filename))
            with open(self.filename, "r") as f:
                result = f.read()
    
            self.assertEqual(result,msg)

    def test_read_file(self):
        # test reading text from a file 
        expected_content = "READ ME!"
        with open(self.filename, "w") as file:
            f.write(expected_content)

        with open(self.filename, "r")as f:
            data = f.read()

        self.assertEqual(data, expected_content)

    def test_appenf_file(self):
        # test appending text to an existing file 
        intial_content = "line one"
        append_content = "\nline two"

        with open(self.filename, "w") as f:
            f.write(intial_content)

        with open(self.filename, "r") as f:
            f.write(append_content)

        with open(self.filename, "r") as f:
            final_datt = f.read()

# run the unit tests automatically when the file is run 
if __name__ == "__main__":
    unittest.main()