import sys
from stack import Stack
from collections import *

def problem2(s,brackets):
    for b in range(len(brackets)):
        kind = startend(brackets[b])
        if(kind == 'start'):
            s.push(brackets[b])
        if(kind == 'end'):
            if(s.is_empty()):
                return False
            if(match(s.pop(),brackets[b])==False):
                return False

    if s.is_empty():
        return True
    else:
        return False

def match(b1,b2):

    if((b1=='{' and b2=='}') or
       (b1=='[' and b2==']') or
       (b1=='<' and b2=='>') or
       (b1=='(' and b2==')')):
       return True
    return False

def startend(bracket):
    start={'{','[','(','<'}
    end={'}',']',')','>'}
    if(bracket in start):
        return 'start'
    elif(bracket in end):
        return 'end'
    else:
        return 'other'

def driver():
    s = Stack()
    f = open(sys.argv[1])
    lines = int(f.readline().strip())
    for l in range(lines):
        brackets = f.readline().strip()
        check = problem2(s, brackets)
        if(check==True):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    driver()
