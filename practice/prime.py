
N = int(input("enter the last number that you want to check starting from zero:"))

def isprime(number):
    for witness in range(2,number):
        if number % witness == 0:
            return(False)
        if witness**2 > number:
            break
    return True

for number in range(2,N):
    if isprime(number):
        print(number)

