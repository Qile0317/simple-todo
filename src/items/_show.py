#a collection of functions to simply convert attributes into strings for __repr__

#completion status can stay the same

#priority character
def priority(priority_letter):
    if priority_letter == "":
        return "( ) "
    return "("+priority_letter+") "

#get the string of a datetime obj + space
def date(time_attr):
    return str(time_attr)[0:19]+" "

#skip task bc its just a string

#get project
def project(proj):
    if proj == "":
        return "+ "
    return "+"+proj+" "

#get context
def context(cont):
    if cont == "":
        return "@ "
    return "@"+cont+" "

#convert the math string
def maths(mathstr):
    if mathstr == "" or mathstr == None:
        return "="
    return "="+mathstr