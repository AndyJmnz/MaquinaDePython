import math
import os
import random
import re
import sys


def timeConversion(s):
    hours = s[:-2]
    period = s[-2:]
    
    hour, minute, second = map(int, hours.split(":"))
    
    if(period == "PM" and hour != 12):
        hour += 12
    if(period == "AM" and hour == 12):
        hour = 0
        
    MilitaryTime = f"{hour:02}:{minute:02}:{second:02}"
    return MilitaryTime
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
