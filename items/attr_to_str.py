#a collection of functions to simply convert attributes into strings for __repr__

#completion status from bool to "x" or ""
def completion(completion_status: bool): 
    if completion_status == True:
        return "x "
    return ""

#priority character
def priority(priority_letter):
    if priority_letter == "":
        return ""
    return "("+priority_letter+") "

#get the yyyy-mm-dd of a datetime obj
def date(time_attr):
    return str(time_attr)[0:10]+" "

#skip task bc its just a string

#get project
def project(proj):
    if proj == "":
        return ""
    return "+"+proj+" "

#get context
def context(cont):
    if cont == "":
        return ""
    return "@"+cont+" "

#convert the math string
def maths(mathstr):
    if mathstr == "" or mathstr == None:
        return ""
    return "+"+mathstr