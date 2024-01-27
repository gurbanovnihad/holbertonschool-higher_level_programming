#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "+":
        print(add(a, b))
    elif operator == "-":
        print(sub(a, b))
    elif operator == "*":
        print(mul(a, b))
    else:
        print(div(a, b))
