#!/usr/bin/python3
from parser import *
#expr = "sin(cos(sin(cos(3.4*x*sin(x)))))"
expr = "sin(x*x)"
print(parser(expr).D().simplify())

