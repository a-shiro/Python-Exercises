def operate(operator, *args):

    if operator == '+':
        result = args[0]
        for x in range(len(args) - 1):
            result += args[x + 1]
        return result
    elif operator == '-':
        result = args[0]
        for x in range(len(args) - 1):
            result -= args[x + 1]
        return result
    elif operator == '*':
        result = args[0]
        for x in range(len(args) - 1):
            result *= args[x + 1]
        return result
    elif operator == '/':
        if 0 not in args:
            result = args[0]
            for x in range(len(args) - 1):
                result /= args[x + 1]
            return result


print(operate('/', 0))