class Bank:
    def __init__(self):
        self.closingBal = 0

    def display(self):
        print("Enter your Options :")
        print("1 for deposit : \n 2 for withdraw :")
        getOption = input()

        if getOption == "1":
            self.deposit()
        elif getOption == "2":
            self.withdraw()
        elif getOption !=1 or getOption !=2:
            print("Thanks")
            return
        print("Your closing balance is :", self.closingBal
        print("Do you want to continue: ")
        a= input()

        if a=="Y" or a== "y":
            self.display()
        else:
            print("Thanks fro visiting our Bank")

    def deposit(self):
        depositAmnt = int(input("Enter Your deposit Amount"))
        self.closingBal = self.closingBal+depositAmnt
        return self.closingBal

    def withdraw(self):
        withdrawAmnt = int(input("Enter your withdraw Amount"))
        if self.closingBal>= withdrawAmnt:
            self.closingBal = self.closingBal - withdrawAmnt
            print("After withdraw your balance amount is :", self.closingBal)
        else:
            print("No sufficient Balance")
            return self.closingBal

bankObj = Bank()
bankObj.display()

