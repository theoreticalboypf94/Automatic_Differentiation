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
            continue        # we don't fall down until zero balance condition - border of expression

        if c in "+-*/":                     # inter-scope group operations
            #print("fint operation", c)     #try to find top priority op. * or / and handle it first
            if minimum is None:
                minimum = i,c
            else:
                _, old = minimum
                if old in "*/" and c in "+-":
                    minimum = i,c
    # that means that we have constant or Function, without +-.. sin(sin(x))
    if minimum is None:
        try:
            return CONST_EXPR(float(string))
        except:
            # TODO add other functions: now only sin cos x
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
        #TODO add / operation and pow() function or ^ or **
        if operation == '+':
            return Expression(ADDop(), [left, right])
        elif operation == '-':
            return Expression(SUBop(), [left, right])
        elif operation == '*':
            return Expression(MULop(), [left, right])
        else:
            assert("ERROR BLIAD" is None)
        

def take_off_brakets(string : str) -> str:
    """
    (a+b) + (c-d) - we don't need to remove brakets from here
    ((((a+b)))))  - we really need to remeve that crap.

    calculate brakets balance,
    """
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
