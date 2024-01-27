#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == "+":
        print(add(a, b))
    elif operator == "-":
        print(sub(a, b))
    elif operator == "/":
        print(div(a, b))
    else:
        print(mul(a, b))
