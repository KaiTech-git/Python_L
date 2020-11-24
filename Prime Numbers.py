
N= int(input('Enter the number '))
if N <= 1:
    print("No prime numbers.")
else:
    for x in range(2,(N+1)):
        j = 0
        for i in range(2,x):

            if x%i != 0:
                continue
            else:
                j=j+1
        if j==0:
            print(x)








