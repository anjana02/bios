def operation(val, stack):
    if val == 1:
        stack.pop(0)
        print(stack)
        print_operation(stack)
    elif val == 2:
        stack.insert(0, str(input()))
        print(stack)
        print_operation(stack)
    else:
        print("Invalid Operation")
        print_operation(stack)


def print_operation(stackList):
    fun = int(input("Which Operation would you like to do on stack \n 1. Pop \n 2. Push \n"))
    operation(fun, stackList)


if __name__ == '__main__':

    n = int(input("Number of Stack Elements:"))
    stack_list = list()
    for i in range(n):
        stack_list.append(input(f"Enter the {i + 1} element:"))

    print_operation(stack_list[::-1])