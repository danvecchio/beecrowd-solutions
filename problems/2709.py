# -*- coding: utf-8 -*-

def isPrime(num):
    if num<=1:
        return False
    elif num<=3:
        return True
    elif num%2==0 or num%3==0:
        return False
    i=5
    while i*i<num:
        if(num%i==0 or num%(i+2)==0):
            return False
        i+=6
    return True
while True:
    try:
        sum=0
        coin_number = int(input())
        coins = [None]*coin_number
        for i in range(coin_number):
            coins[i]=int(input())
        jump = int(input())
        i=coin_number-1
        while i>=0:
            sum+=coins[i]
            i-=jump
        #print(sum)
        if(isPrime(sum)):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
    except EOFError:
        break

