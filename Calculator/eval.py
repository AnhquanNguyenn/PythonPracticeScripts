# Function to find precedence
# of operators.


def precedence(op):

    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

# Function to perform arithmetic
# operations.


def applyOp(a, b, op):

    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a // b

# Function that returns value of
# expression after evaluation.


def eval(expression):

    # stack to store integer values.
    values = []

    # stack to store operators.
    ops = []
    i = 0
    sign = 1

    while i < len(expression):
        if expression[i] == '-':
            sign = -1
            expression = expression[1:]
            continue

        # Current token is a whitespace,
        # skip it.
        if expression[i] == ' ':
            i += 1
            continue

        # Current token is an opening
        # brace, push it to 'ops'
        elif expression[i] == '(':
            ops.append(expression[i])

        # Current token is a number, push
        # it to stack for numbers.
        elif expression[i].isdigit():
            val = 0

            # There may be more than one
            # digits in the number.
            while (i < len(expression) and
                   expression[i].isdigit()):

                val = (val * 10) + int(expression[i])
                i += 1

            values.append(val)

        # Closing brace encountered,
        # solve entire brace.
        elif expression[i] == ')':

            while len(ops) != 0 and ops[-1] != '(':

                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # pop opening brace.
            ops.pop()

        # Current token is an operator.
        else:

            # While top of 'ops' has same or
            # greater precedence to current
            # token, which is an operator.
            # Apply operator on top of 'ops'
            # to top two elements in values stack.
            while (len(ops) != 0 and
                   precedence(ops[-1]) >= precedence(expression[i])):

                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(applyOp(val1, val2, op))

            # Push current token to 'ops'.
            ops.append(expression[i])

        i += 1

    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops) != 0:

        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(applyOp(val1, val2, op))

    # Top of 'values' contains result,
    # return it.
    return values[-1] * sign


# Driver Code
if __name__ == "__main__":

    print(eval("10 + 2 * 6"))
    print(eval("100 * 2 + 12"))
    print(eval("100 * ( 2 + 12 )"))
    print(eval("100 * ( 2 + 12 ) / 14"))
    print(eval('- (3 + ( 2 - 1 ) )'))
