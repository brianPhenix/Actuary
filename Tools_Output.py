from Actuary_Header import *

def printReadable(p):


    class P():
        COL_TOTAL     = 5    
        COL_N         = 0
        INPUT_NAME    = "None"
        TAG           = p["name"]
        OUT           = "None"

    def newline():
        n=0
        if P.COL_N % P.COL_TOTAL == 0: 
            n=1
        return(n)
            
    def newlineMake():
        P.OUT+= "\n"
        return(None)
           

    def DoPrintReadable(p):
        isDone=0
        P.OUT="\n"
        d = {k:v for (k,v) in p.items() if v == 1 or v == 0}
        P.OUT+= "{}:\n".format(P.TAG)
        for x in d :
            P.COL_N+=1
            P.OUT+="{}".format(x).rjust(10," ")
            if newline(): newlineMake()
            if x==1996 : 
                P.OUT += "".rjust(10, " ")
                P.COL_N  += 1
                if newline(): newlineMake()
        isDone=1
        return(isDone)

    
    def PrintReadable(p):
        if( DoPrintReadable(p) ): 
            print(P.OUT)

    PrintReadable(p)





