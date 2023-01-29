import unittest

#dependencies
import datetime as dt

#the imports are completely screwed up lol
import os
import sys

#insert parent dir path???
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__name__), '..')))

#items folder
from src.items import _show
from src.items import todo_item as todo 

#__init__ can be assumed to work

# testing the _show functions, but tbh they are super simple
class _Test_show(unittest.TestCase):
    def test__show(self):

        self.assertEqual(_show.priority(""),"( ) ")
        self.assertEqual(_show.priority("A"),"(A) ")

        self.assertEqual(_show.date(dt.datetime(year=2420,
        month=12,day=2,hour=6,minute=9,second = 1)),"2420-12-02 06:09:01 ")
        self.assertEqual(_show.date(dt.datetime(year=2420,
        month=12,day=2,hour=6,minute=9,second = 1,microsecond = 69420)),
        "2420-12-02 06:09:01 ")

        self.assertEqual(_show.project(""),"+ ")
        self.assertEqual(_show.project("placeholder"),"+placeholder ")

        self.assertEqual(_show.context("placeholder"),"@placeholder ")
        self.assertEqual(_show.context(""),"@ ")

        self.assertEqual(_show.maths(""),"=")
        self.assertEqual(_show.maths("69/420"),"=69/420")

#testing the defeault empty string of the item object
class _TestStr(unittest.TestCase):
    def test_str(self):
        test_item = str(todo.item())
        self.assertEqual(len(test_item),68)
        self.assertEqual(test_item[0:6], '- ( ) ')
        self.assertEqual(test_item[46:67], "placeholder_task + @ ") 

# testing the readline function
class _TestRead(unittest.TestCase):
    def test_read(self):
        # create item object
        test_item = todo.item(completion = "x", priority = "Q",
                              startdate=dt.datetime(year=2005,
                                                    month=3,day=17),
                              enddate=dt.datetime(year= 2022,month =6,
                                                  day = 7, hour = 15,
                                                  minute=12,second=1),
                              task="living on earth",project = "live",
                              context = "none",maths = "69 + 420"
                              )
        
        # test that the item was correctly created
        str_test_item = str(test_item)
        self.assertEqual(len(str_test_item),83)
        self.assertEqual(str_test_item, "x (Q) 2005-03-17 00:00:00 2022-06-07 15:12:01 living on earth +live @none =69 + 420")

        # test the actual readline function
        newline_normal = "- (J) 2006-11-12 00:00:00 2022-06-07 15:12:01 placeholder placeholder +placeholder @placeholder =999*7"
        test_item.readline(newline_normal)
        self.assertEqual(str(test_item),newline_normal)

#todo.item.append() can be assumed to work due to its simplicity

# conduct tests
if __name__ == '__main__':
    unittest.main()