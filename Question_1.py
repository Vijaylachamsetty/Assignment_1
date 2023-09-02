n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2 , end="\n")
for i in range(2,51):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3>=50:
        break
    print(n3, end="\n")
print()
