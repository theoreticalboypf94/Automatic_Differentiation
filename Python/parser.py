from try2 import *

def parser(string : str) -> Expression:
    balance = 0
    minimum = None
    #print(string)
    string = string.replace(' ', '');
    string = take_off_brakets(string);
    #print(string)
    for i,c in enumerate(string):
        if c == "(":
            balance += 1
        elif c == ")":
            balance -= 1
        if balance!=0:
            continue

        if c in "+-*/":
            #print("fint operation", c)
            if minimum is None:
                minimum = i,c
            else:
                _, old = minimum
                if old in "*/" and c in "+-":
                    minimum = i,c
    if minimum is None:
        try:
            return CONST_EXPR(float(string))
        except:
            if string[0] == "s":
                arg = parser(string[4:-1])
                return Expression(Function_sin(), [arg])

            if string[0] == "c":
                arg = parser(string[4:-1])
                return Expression(Function_cos(), [arg])

            if string[0] == 'x':
                return VAR()
            assert(False)
    else:
        index, operation = minimum
        left, right = parser(string[:index]), parser(string[index+1:])
        if operation == '+':
            return Expression(ADDop(), [left, right])
        elif operation == '-':
            return Expression(SUBop(), [left, right])
        elif operation == '*':
            return Expression(MULop(), [left, right])
        else:
            assert("ERROR BLIAD" is None)
        

    


def take_off_brakets(string : str) -> str:
    if string[0] == "(" and string[-1] == ")":
        balance = 0
        for i,c in enumerate(string):
            if c == "(":
                balance += 1
            elif c == ")":
                balance -= 1
            if balance == 0 and i != len(string)-1:
                return string

        return take_off_brakets(string[1:-1])
    else:
        return string


        

