from Actuary_Header import *



def isLeapYear(year):
    if year==2000: 
        return(0)
    elif (year % 4)==0:
        return(1)
    else:
        return(0)

def setDictLeapYear(start=1900, nY=200):
    clearDictLeapYear()
    Dict.LeapYear["start"]=start
    Dict.LeapYear["end"]  =start + nY
    for i in range(nY):
        index = start + i
        Dict.LeapYear[index]= isLeapYear(index)



def setIsLeapYear(p):
    Dict.IsLeapYear.clear
    Dict.IsLeapYear = {k:v for (k,v) in p.items() if v == 1}
    for (k,v) in p.items(): 
        if type(k)==str: 
            Dict.IsLeapYear[k] = Dict.LeapYear[k]
    Dict.IsLeapYear["name"]=Name.IsLeapYear
            

def setNotLeapYear(p):
    Dict.NotLeapYear.clear
    Dict.NotLeapYear = {k:v for (k,v) in p.items() if v == 0}
    for (k,v) in p.items(): 
        if type(k)==str: 
            Dict.NotLeapYear[k] = Dict.LeapYear[k]
    Dict.NotLeapYear["name"]=Name.NotLeapYear


def clearDictLeapYear(): 
    d = { "name": Dict.LeapYear["name"] }
    Dict.LeapYear.clear()
    Dict.IsLeapYear.clear()
    Dict.NotLeapYear.clear()

    Dict.LeapYear = d

 




