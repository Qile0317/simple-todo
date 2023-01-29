import unittest

#dependency
import datetime as dt

#items folder
from items import _show
from items import todo_item as todo #__init__ can be assumed to work

"""
#testing the _show functions - unfinished: if someone can write some cases for all functions in items/_show.py it'd be nice
class _Test_show(unittest.TestCase):
    def test__show(self):
        self.assertEqual()
"""

#testing the defeault empty string of the item object
class _TestStr(unittest.TestCase):
    def test_str(self):
        test_item = str(todo.item())
        self.assertEqual(len(test_item),51)
        self.assertEqual(test_item[0:6], '- ( ) ')
        self.assertEqual(test_item[45:52], " + @ =") 
        # so theres an extra space between the "+" and the time before it...
        #fix? or keep?

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
"""
        # test the actual readline function - doesn't work i messed up something in the code
        # this code should take the "newline" string and make it the attributes of the item object.
        # it insteads makes it:
        # "- (J) 2006-11-12 00:00:00 2022-06-07 15:12:01 placeholder placeholde ++placeholder  @ ="
        # instead of the string below.
        
        newline = "- (J) 2006-11-12 00:00:00 2022-06-07 15:12:01 placeholder placeholder +placeholder   @placeholder =999*7"
        test_item.readline(newline)
        self.assertEqual(str(test_item),newline)
"""
#todo.item.append() can be assumed to work due to its simplicity

# conduct tests
if __name__ == '__main__':
    unittest.main()