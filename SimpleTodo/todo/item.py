# item class, for the todo list, follows the todo.txt structure
# this script should be imported as "todo" as the class item can be used as "todo.item()"

import datetime as dt
from .format import TodoEncoder, TodoDecoder 

class Item:
    
    def __init__(self,
        is_finished: bool = False,
        priority: str = " ", 
        start_date: dt.datetime = dt.datetime.now(),
        end_date: dt.datetime = dt.datetime.now()+dt.timedelta(weeks=1),
        task: str = "placeholder_task",
        project: str = "",
        context: str = "",
        maths: str = ""
    ) -> None:
        
        self.is_finished = is_finished
        self.priority = priority
        self.start_date = start_date
        self.end_date = end_date
        self.task = task
        self.project = project
        self.context = context
        self.maths = maths
    
    @property
    def attributes(self):
        return [
            self.is_finished,
            self.priority,
            self.start_date,
            self.end_date,
            self.task,
            self.project,
            self.context,
            self.maths,
        ]
    
    def __repr__(self) -> str:
        return TodoEncoder.to_string(*self.attributes)
    
    @classmethod
    def from_string(cls, string: str):
        return cls(*TodoDecoder.from_string(string))
    
    #append the todo item into the todo.txt file for storage
    def append(self, file_str = "data/todo.txt"):
        with open(file_str, "a") as file:
            file.write(str(self)+"\n")