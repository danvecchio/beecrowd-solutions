#check if n is 'prime' or 'not prime'
def is_prime(n):
    if(n==2 or n==3):
        print("Prime")
        return
    if (n % 2 == 0 or n % 3 == 0) :
        print("Not Prime")
        return    
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            print("Not Prime")
            return
        i = i + 6

    print("Prime")

#Get user input
n = int(input())

#loop between 0 and n-1
for i in range(n):
    prime = int(input())
    is_prime(prime)