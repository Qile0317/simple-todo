#a collection of functions to simply convert attributes into strings for __repr__

import datetime as dt

#completion status can stay the same

#priority character
def priority(priority_letter):
    if priority_letter == "":
        return "( ) "
    return "("+priority_letter+") "

#get the string of a datetime obj + space. Also allows "" or None
def date(time_attr):
    if time_attr != "" and time_attr != None:
        return str(time_attr)[0:19]+" "
    return "yyyy-mm-dd hh:mm:ss "

# while reading in a line in todo.txt, date may be empty
def convert_date(datestr):
    if datestr != "yyyy-mm-dd hh:mm:ss":
        return dt.datetime.strptime(datestr,"%Y-%m-%d %H:%M:%S")
    return datestr

#skip task bc its just a string

#get project
def project(proj):
    if proj == "":
        return "+ "
    return "+" + proj + " "

#get context
def context(cont):
    if cont == "":
        return "@ "
    return "@" + cont + " "

#convert the math string
def maths(mathstr):
    if mathstr == "" or mathstr == None:
        return "="
    return "=" + mathstr