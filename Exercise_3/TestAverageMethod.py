import unittest
from average import average

class TestAverageMethod(unittest.TestCase):
    
    def test_case_1(self):
        # TC1: Không có phần tử hợp lệ
        self.assertEqual(average([], 0, 100), -999)
    
    def test_case_2(self):
        # TC2: Vòng lặp chạy nhưng không có phần tử hợp lệ trong khoảng [minimum, maximum]
        self.assertEqual(average([101, -5, -999], 0, 100), -999)
    
    def test_case_3(self):
        # TC3: Nhiều giá trị hợp lệ nằm trong khoảng [minimum, maximum]
        self.assertEqual(average([20, 30, 40, -999], 0, 50), 30.0)
    
    def test_case_4(self):
        # TC4: Hỗn hợp giá trị hợp lệ và không hợp lệ
        self.assertEqual(average([150, 25, 50, -999], 0, 100), 37.5)

if __name__ == "__main__":
    unittest.main()
