#item class, for the todo list, follows the todo.txt structure
#this script should be imported as "todo" as the class item can be used as "todo.item()"

import datetime as dt # done in __init__.py in main though?
from items import _show 

#may need to rename
class item: 
    def __init__(self, completion = "-", priority = "", 
                 startdate = dt.datetime.now(),
                 enddate = dt.datetime.now()+dt.timedelta(weeks=1),
                 task ="",project="",context="",maths ="") -> None:
        self.completion = completion # str: x or - (completed or incomplete)
        self.priority = priority # str: A - Z or ""
        self.startdate = startdate # dt.datetime
        self.enddate = enddate # dt.datetime
        self.task = task # str
        self.project = project # str
        self.context = context # str
        self.maths = maths # str (could be parsed)
    
    # return the attributes in the format of:
    # x (A) YYYY-mm-dd HH:MM:SS YYYY-mm-dd HH:MM:SS task +project @context =2+2
    def __str__(self) -> str:
        returnstr = self.completion + " "
        returnstr += _show.priority(self.priority)
        returnstr += _show.date(self.startdate)
        returnstr += _show.date(self.enddate)
        returnstr += self.task + " "
        returnstr += _show.project(self.project)
        returnstr += _show.context(self.context)
        returnstr += _show.maths(self.maths)
        return returnstr

    #takes a string of a todo.txt file line and overwrites the todo_item attributes
    #TODO: test this! 
    def read(self, line:str):
        self.completion = line[0] 
        self.priority = line[3]
        self.startdate = dt.datetime.strptime(line[6:25] ,"%Y-%m-%d %H:%M:%S")
        self.enddate = dt.datetime.strptime(line[27:45] ,"%Y-%m-%d %H:%M:%S")
        
        #getting task, project, context, maths
        n = len(line)
        for i in range(46,n):
            curr_char = line[i]

            if curr_char == "+":
                self.task = line[46:i-2]
                project_start_ind = i
            if curr_char == "@":
                self.project = line[project_start_ind:i-2]
                maths_start_ind = i
            if i == n:
                self.maths = line[maths_start_ind:n]