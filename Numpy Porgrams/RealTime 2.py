import numpy as np
a=np.array([["Lara","10","29"],
            ["Mani","20","12"],
            ["Maha","30","15"]])
print(a[...,0])
print("===============")
print(a[...,1])
print("===============")
print(a[...,2])
print("===============")
loan_amount=a[...,2]
print(loan_amount)
print("===============")
print(type(loan_amount))
print("===============")
y=loan_amount.astype(int)
print(type(loan_amount))
print("================")
print(sum(y))