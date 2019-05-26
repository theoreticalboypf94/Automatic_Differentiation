#!/usr/bin/python3

# this file is simple prototype for automatic differentiation of input text file
# main concept here is that that I have two thing Function and Operation (united in class Gramatika)
# We parse input text messege which contain function i.e. 'f(x) = exp(x**3.14) + cos(arcsin(2./x)) -o1)
# -o 1 -is order of searching derivateve

# we have binary operation which unite function together : for + 'f() = function1 + function2' here to get derivative of common function we finde derivatives of subfunctions untill we either get 0 or constant



#expression = input()

#print("\nYou pass: ", expression)

class Expression:

    class Function:
        __func_neme = "exp,sin,cos,ln"

        @staticmethod
        def parser(f_str):
            # this is simple parser which separete signature from scope
            signatura =''
            argument = ''
            sig = True
            for i in f_str:
                if i != '(' and sig:
                    signatura += i
                elif i== '(' and sig:
                    # firs collision of ( scope
                    sig == False
                else:
                    argument += i
            argument = argument[:-1] #remote last scope )
            result = [signatura, argument]
            return result



        def __init__(self, function_as_string):
            self.signature = self.parser(function_as_string)[0]
            self.argument = self.parser(function_as_string)[1]

    class Operation:
        __op_name = "+-*/"
        pass

    def __init__(self, str_toparse):
        self.exp_list = []
        self.exp_list = parse(str_toparse)

    def parse(self, str_arg):
        result = []

        return result



if __name__ == "__main__":
    expression_test = "f(x) = exp(x^3.14) + cos(sqrt(x+1) + x) * (x + sin(x))"
    #segregate function and rithmetic operation
    left,right = 0,0
    OP = "+-*/=^"
    result_list = []
    expression_test = expression_test.replace(' ', '')
    counter_of_right_scope = 0
    for i in range(len(expression_test)):
        if expression_test[i] in OP and counter_of_right_scope == 0:
            right = i
            result_list.append(expression_test[left:right])
            result_list.append(expression_test[i])
            left = i+1
        if expression_test[i] == '(' and i == left:
            # скобочка после операции тождественна скобочки порядка
            counter_of_right_scope = 1

        if counter_of_right_scope !=0:

    result_list.append(expression_test[left:i])

    print(result_list)

