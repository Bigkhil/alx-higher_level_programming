#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    operator = sys.argv[2]
    if op == '+':
        print("{} + {} = {}".format(num1, num2, calculator_1.add(num1, num2)))
    elif op == '-':
        print("{} - {} = {}".format(num1, num2, calculator_1.sub(num1, num2)))
    elif op == '*':
        print("{} * {} = {}".format(num1, num2, calculator_1.mul(num1, num2)))
    elif op == '/':
        print("{} / {} = {}".format(num1, num2, calculator_1.div(num1, num2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
