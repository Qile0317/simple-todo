#item class, for the todo list, follows the todo.txt structure

import datetime as dt # done in __init__.py in main though?
from items import attr_to_str as _show 

class todo_item:
    def __init__(self, completion = False, priority = "", 
                 startdate = dt.datetime.now(),
                 enddate = dt.datetime.now()+dt.timedelta(weeks=1),
                 task ="",project="",context="",maths ="") -> None:
        self.completion = completion # bool: True or False
        self.priority = priority # str: A - Z or ""
        self.startdate = startdate # dt.datetime
        self.enddate = enddate # dt.datetime
        self.task = task # str
        self.project = project # str
        self.context = project # str
        self.maths = project # str (could be parsed)
    
    # return the attributes in the format of:
    #  x (A) yyyy-mm-dd yyyy-mm-dd task +project @context =2+2
    def __repr__(self) -> str:
        returnstr = _show.completion(self.completion)
        returnstr += _show.priority(self.priority)
        returnstr += _show.date(self.startdate)
        returnstr += _show.date(self.enddate)
        returnstr += self.task+" "
        returnstr += _show.project(self.project)
        returnstr += _show.context(self.context)
        returnstr += _show.maths(self.maths)
        return returnstr
