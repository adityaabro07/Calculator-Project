def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

Operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}
def calculator():
    should_continue = True
    first_number = float(input("Enter the first number:\n "))
    while should_continue:
        operation_to_perform = input("Enter the operation:\n+\n_\n*\n/\n")
        second_number = float(input("Enter the second number:\n "))
        answer=Operations[operation_to_perform](first_number, second_number)
        print(f"{first_number} {operation_to_perform} {second_number}: {answer}")

        choice=input("Type 'y' to continue with the previous calculations and 'n' to continue with the new calculation\n")
        if choice=="y":
            first_number=answer
        elif choice=="n":
            should_continue=False
            print("\n"*20)
            calculator()

calculator()
