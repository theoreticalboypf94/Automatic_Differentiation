#programm based on two class 
# gramma is Expression = Expression Operation Expression or Operation(Expression)

class Expression:
    """
    interface class over possible math expression.
    """
    operation = ''
    arguments = []
    def __init__(self, oper, args):
        self.operation = oper
        self.arguments = args
    def D(self):
        return self.operation.D(self.arguments)
    
    def __repr__(self):
        return self.operation.to_string(self.arguments)

    def simplify(self):
        """
        element vise use simplify method for each extention element
        """
        #print(self.arguments, list(map(type,self.arguments)))
        return self.operation.simplify(list(map(lambda x: x.simplify(), self.arguments)))

 
class Operation:
    """
    interface class over possible operation.
    """
    def simplify(self,args):
        return Expression(self, args)
    def D(self, args):
        pass

class Function_sin (Operation):
    """
    D(sin(x)) = cos(x);
    sin'(f(x)) == cos(f(x)) * f'(x) == cos(f(x)) * D(f(x));
    """
    def D(self,args):
       exp = Expression(Function_cos(), args)
       return Expression(MULop(), [exp, args[0].D()])

    def __repr__(self):
       return "sin"

    def to_string(self, args):
       return "sin(%s)" % (args[0])

class Function_cos (Operation):
    """
    D(cos(x)) = -sin(x);
    cos'(f(x)) == -sin(f(x)) * f'(x) == -sin(f(x)) * D(f(x));
    """
    def D(self, args):
        exp = Expression(Function_sin(), args)
        tmp = Expression(MULop(), [exp, args[0].D()])
        return Expression(MULop(), [CONST_EXPR('-1'), tmp])

    def __repr__(self):
        return "cos"

    def to_string(self, args):
        return "cos(%s)" % (args[0])

class VAR(Expression):
    """
    pure x, without anything else;
    may be in future that will cause trouble
    becouse I try to add power ^ operation
    """
    def simplify(self):
        return self
    def __init__(self):
        pass
    def D(self):
        return CONST_EXPR("1")
    def __repr__(self):
        return "x"

class CONST_EXPR(Expression):
    # value = ''
    def simplify(self):
        return self
    def __init__(self, val):
        self.val = val
    def D(self):
        return CONST_EXPR(0)
    
    def __repr__(self):
        return str(self.val)

class ADDop (Operation):
   
    def simplify(self, args):
        """
        0 + something == something + 0 == something
        """
        if type(args[0]) is CONST_EXPR:
            if args[0].val == 0:
                return args[1]
        if type(args[1]) is CONST_EXPR:
            if args[1].val == 0:
                return args[0]
        return Expression(self, args)

    def D(self, args):
        return Expression(self, [args[0].D(), args[1].D()])

    def to_string(self, arg):
        return "%s + %s" % (arg[0], arg[1])

class SUBop (Operation):

    def simplify(self, args):
        """
        sence equal to ADDop.simplify
        """
        if type(args[0]) is CONST_EXPR:
            if args[0].val == 0:
                return Expression(MULop(), [CONST_EXPR(-1), args[1]])
        if type(args[1]) is CONST_EXPR:
            if args[1].val == 0:
                return args[0]
        return Expression(self, args)
    def D(self, args):
        return Expression(self, [args[0].D(), args[1].D()])
    def to_string(self, arg):
        return "%s - %s" % (arg[0], arg[1])

class MULop (Operation):
    
    def simplify(self, args):
        """
        0 * something == something * 0 == 0;
        """
        if type(args[0]) is CONST_EXPR:
            if args[0].val == 0:
                return args[0]
        if type(args[1]) is CONST_EXPR:
            if args[1].val == 0:
                return args[1]
        return Expression(self, args)
    def D(self, args):
        expression1 = Expression(self, [args[0].D(), args[1]])
        expression2 = Expression(self, [args[0], args[1].D()])
        return Expression(ADDop(), [expression1, expression2])
    def to_string(self, arg):
        return "(%s)*(%s)" % (arg[0], arg[1])
    
