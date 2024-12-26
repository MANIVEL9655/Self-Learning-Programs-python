import numpy as np
a=np.array([["Lara","10","29"],
            ["Mani","20","12"],
            ["Maha","30","15"]])
print("Names of all who applied Loan with ICICI")
print(a[...,0])
print("CBIL SCORE of all who applied wiht ICICI")
print(a[...,1])
print("Loan Amount")
loan_amount = (a[...,2])
d=list(loan_amount)
print(d)
total_amount_needed=int(input("Enter the needed amount"))
for loan in d:
    loan = int(loan)
    total_amount_loan_needed=total_amount_needed+loan
    print("Branch office need {} Lakhs to dispuse all loans".format(total_amount_loan_needed))