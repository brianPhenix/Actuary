
from ast import DictComp
from Actuary_Header import *
from Actuary import *

from Tools_Output import printReadable


setDictLeapYear(1960, 100)
setIsLeapYear( Dict.LeapYear )
setNotLeapYear( Dict.LeapYear )


printReadable( Dict.IsLeapYear )
printReadable( Dict.NotLeapYear )




