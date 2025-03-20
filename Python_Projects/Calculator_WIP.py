def is_integer(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

def check_expression(input):
    if input == "*":
        return True
    elif input == "/":
        return True
    elif input == "+":
        return True
    elif input == "-":
        return True
    else:
        return False

def checkInput(input):
    if input == "quit":
        print("Quitting...")
        quit()
    elif is_integer(input):    # can go through and find out if input is an integer
        return input
    else:
        if check_expression(input):
            return input
        else:
            input = None
            print("Please enter a valid number!")
            return input

def check_ActiveExpression(expression):
    if expression:
        return True


class Input:
    def __init__(self):
        check_ActiveExpression()
        self._input = input("Enter a number or expression\nor calc to calculate\nor quit to quit\n: ")
        self._input = self._input.strip()
        self._input = self._input.lower()
        self._input = self._input.replace(" ", "")
        

        if self._input == "calc":
            print("Calculating...")
            calculate()

        checkInput(self._input)



def DisplayCalc(input):
    print(input)


def calculate():
    print("Calculating...")

def main():
    input_list = []
    while True:
        input_list.append(Input())
        DisplayCalc(input_list)

main()
