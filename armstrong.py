# Armstrong Number Program

num = int(input("Enter a number: "))
n = len(str(num))   
sum_val = 0
steps = []          

for ch in str(num):       
    digit = int(ch)
    power = digit ** n
    sum_val += power
    steps.append("*".join([str(digit)] * n))

calculation = " + ".join(steps)
print(calculation, "=", sum_val)

if sum_val == num:
    print("Yes")
    print(num, "is an Armstrong number.")
else:
    print("No")
    print(num, "is not an Armstrong number.")
