import SimpleTodo as Todo
import datetime as dt

"""
# need to incorporate something similar to readline() to modify the curr obj
def test_sparse_decode():
    newline_sparse = "x ( ) yyyy-mm-dd hh:mm:ss 2023-03-14 19:00:00 do this simple task + @ ="
    test_item = Todo.Item()
    test_item.readline(newline_sparse)
    assert str(test_item) == newline_sparse
"""

#test encoder and decoder (need to first test encoder, then decoder)
def test_todo_format():
    todo = "x (A) 1969-07-16 13:32:00 1969-07-20 20:17:00 Land on the moon +Space @Moon =2+2"
    assert Todo.TodoEncoder.to_string(*Todo.TodoDecoder.from_string(todo)) == todo

def test_item_init():
    test_item = str(Todo.Item())
    assert test_item[0:5] == '- ( )'

"""
# unfinished, just wanted to test encoding and the attributes
def test_item_args():
    test_item = Todo.Item(completion = "x", priority = "Q",
                              startdate=dt.datetime(year=2005,
                                                    month=3,day=17),
                              enddate=dt.datetime(year= 2022,month =6,
                                                  day = 7, hour = 15,
                                                  minute=12,second=1),
                              task="living on earth",project = "live",
                              context = "none",maths = "69 + 420"
                              )
"""

def test_attributes():
    todo_Item = Todo.TodoDecoder.from_string(
        "x (A) 2023-01-29 15:33:25 2023-01-29 15:33:25 task +project @context =2+2")
    assert todo_Item ==[True, 'A', dt.datetime(2023, 1, 29, 15, 33, 25), 
                        dt.datetime(2023, 1, 29, 15, 33, 25), 'task', 
                        'project', 'context', '2+2']
