import unittest
from items import todo_item as todo

#dunno why this script isn't working for me /Qile

class TestCalculate(unittest.TestCase):
    def test_repr(self):
        test_item = todo.item()
        self.assertEqual( str(test_item), "placeholder")

#Also need to test the item.read() function

# conduct tests
if __name__ == '__main__':
    unittest.main()