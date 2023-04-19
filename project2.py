rows = {'a': 0, '+': 1, '-': 2, '*': 3, '/': 4, '(': 5, ')': 6, '$': 7}
columns = {'E': 0, 'Q': 1, 'T': 2, 'R': 3, 'F': 4}
table = [
    ["TQ", None, None, None, None, "TQ", None, None],
    [None, "+TQ", "-TQ", None, None, None, '', ''],
    ["FR", None, None, None, None, "FR", None, None],
    [None, '', '', "*FR", "/FR", None, '', ''],
    ["a", None, None, None, None, "(E)", None, None]
]

def print_results(input_out, stack, result):
    print("Input:", input_out)
    print("Stack:", end='')
    for item in stack:
        print(item)
    print("Output:", result)


def check_valid(input):
    start = "E$"
    input_out = input
    stack = []
    result = None

    done = False
    while not done:
        s1 = start[0]
        i1 = input[0]

        production = None
        if s1 not in rows:
            production = table[columns[s1]][rows[i1]]

        if start[0] == '$' and input[0] == '$':
            stack.append([start, input, "Accepted"])
            result = 'String is accepted/ valid.'
            done = True
        elif s1 == i1:
            stack.append([start, input, "Reduce"])
            start = start.replace(s1, '', 1)
            input = input.replace(i1, '', 1)
        elif production or production == '':
            stack.append([start, input, production])
            start = start.replace(start[0], production, 1)
        else:
            result = 'String is not accepted/ In valid.'
            done = True

    print_results(input_out, stack, result)

def main():
    # ---- Test Inputs ----
    input = "(a+a)*a$"
    # input = "a*(a/a)$"
    # input = "a(a+a)$"

    check_valid(input)

if __name__ == "__main__":
    main()