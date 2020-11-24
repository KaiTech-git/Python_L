N= int(input('Enter the number '))
S=1000000 # Maximum number that may be given in the programme
k=0  # initialisation of a variable counting how many first numbers have already been displayed
for x in range(2,(S+1)):
    if k == N:
        break
    else:
        j = 0 # initialisation of a variabl
        for i in range(2,x):
            if x%i != 0:
                continue
            else:
                j=j+1
        if j==0:
            print(x)
            k=k+1

