columns = {"a": 0, "+": 1, "-": 2, "*": 3, "/": 4, "(": 5, ")": 6, "$": 7}
rows = {"E": 0, "Q": 1, "T": 2, "R": 3, "F": 4}
table = [
    ["TQ", None, None, None, None, "TQ", None, None],
    [None, "+TQ", "-TQ", None, None, None, "", ""],
    ["FR", None, None, None, None, "FR", None, None],
    [None, "", "", "*FR", "/FR", None, "", ""],
    ["a", None, None, None, None, "(E)", None, None],
]


def print_results(initial_input, stack_steps, result_string):
    print(f"Input: {initial_input}")
    print("Stack: ", end="")
    for stack_step in stack_steps:
        print(stack_step)
    print(f"Output: {result_string}")


def check_valid(input):
    current_stack = "E$"
    input_to_process = input
    stack_steps = []
    result_string = "String is not accepted/ In valid."

    while True:
        first_of_stack = current_stack[0]
        first_of_input = input_to_process[0]

        action = None
        if first_of_stack not in columns.keys():
            action = table[rows[first_of_stack]][columns[first_of_input]]

        if current_stack[0] == "$" and input_to_process[0] == "$":
            stack_steps.append([current_stack, input_to_process, "Accepted"])
            result_string = "String is accepted/ valid."
            break
        elif first_of_stack == first_of_input:
            stack_steps.append([current_stack, input_to_process, "Reduce"])
            current_stack = current_stack.replace(first_of_stack, "", 1)
            input_to_process = input_to_process.replace(first_of_input, "", 1)
        elif action or action == "":
            stack_steps.append([current_stack, input_to_process, action])
            current_stack = current_stack.replace(current_stack[0], action, 1)
        else:
            break

    print_results(input, stack_steps, result_string)


def main():
    # ---- Test Inputs ----
    inputs = ["(a+a)*a$", "a*(a/a)$", "a(a+a)$"]
    # inputs = ["(a+a)*a$"]
    for input in inputs:
        check_valid(input)


if __name__ == "__main__":
    main()
