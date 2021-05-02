import unittest
import os
from ..memory.file_system.save import Save

class TestTimer(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("test.csv")
        except:
            pass
        self.save = Save("test.csv")

        with open("invalid.csv", "w") as file:
            file.write("eifhwiejflewq")

        with open("valid.csv", "w") as file:
            file.write("5,4,3,0,0,0,0,0,0,0")

        self.invalid = Save("invalid.csv")
        self.valid = Save("valid.csv")
        self.empty = [0 for i in range(10)]
    
    def test_missing_file_results_in_empty_leaderboard(self):
        res = self.save.result
        self.assertEqual(res, self.empty)

    def test_invalid_files_turn_valid(self):
        res = self.invalid.result
        self.assertEqual(res, self.empty)
    
    def test_valid_file_read_correctly(self):
        correct = [5,4,3,0,0,0,0,0,0,0]
        res = self.valid.result
        self.assertEqual(correct, res)
    
    def test_update_works_with_valid_input(self):
        self.save.update(23)
        correct = [23,0,0,0,0,0,0,0,0,0]
        res = self.save.result
        self.assertEqual(correct, res)
    
    def test_update_does_not_update_with_string_input(self):
        self.save.update("fjelqfkea")
        res = self.save.result
        self.assertEqual(self.empty, res)
        
    def test_update_does_not_update_with_too_large_input(self):
        self.save.update(10000000000)
        res = self.save.result
        self.assertEqual(res, self.empty)
    
    def test_update_does_not_update_with_too_small_input(self):
        self.save.update(-1)
        res = self.save.result
        self.assertEqual(res, self.empty)
    

    def test_file_in_wrong_order_results_in_empty_file(self):
        with open("test.csv", "w") as file:
            file.write("93,34,1000,0,0,0,0,0,0,0")
        save = Save("test.csv")
        res = save.result
        self.assertEqual(res, self.empty)
    
    def test_file_with_too_large_number_results_in_empty_file(self):
        with open("test.csv", "w") as file:
            file.write("9300000000,34,0,0,0,0,0,0,0,0")
        save = Save("test.csv")
        res = save.result
        self.assertEqual(res, self.empty)
    
    def test_file_with_too_small_number_results_in_empty_file(self):
        with open("test.csv", "w") as file:
            file.write("10,0,0,0,0,0,0,0,0,-1")
        save = Save("test.csv")
        res = save.result
        self.assertEqual(res, self.empty)
    
    def test_file_with_too_short_list_results_in_empty_file(self):
        with open("test.csv", "w") as file:
            file.write("10,0,0")
        save = Save("test.csv")
        res = save.result
        self.assertEqual(res, self.empty)
