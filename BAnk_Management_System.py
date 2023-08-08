def Instruction():
    print(f""" 
          
    Welcome in Bank of India.
                        
    1. Open New Account
    2. Deposit Account
    3. Withdraw Account
    4. Balance Enquiry
    5. Display Customer Details
    6. Deactivate Account
""")


Instruction()
option = int(input("Choose your option : "))


def openAcc():
    pass


def depositAcc():
    pass


def withdrawAcc():
    pass


def balanceEnq():
    pass


def displayDetails():
    pass


def deactivateAcc():
    pass


def main():
    match(option):
        case 1:
            openAcc()

        case 2:
            depositAcc()

        case 3:
            withdrawAcc()

        case 4:
            balanceEnq()

        case 5:
            displayDetails()

        case 6:
            deactivateAcc()

        case _:
            print("Invalid input.")
            Instruction()
