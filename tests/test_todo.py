
import SimpleTodo
from screeninfo import get_monitors

def test_todo_format():
    todo = "x (A) 2023-01-29 15:33:25 2023-01-29 15:33:25 task +project @context =2+2"
    assert SimpleTodo.TodoEncoder.to_string(*SimpleTodo.TodoDecoder.from_string(todo)) == todo
