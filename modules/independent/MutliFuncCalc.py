import os

def primeFact(num):
    # os.system(clear)
    pass

def sqr(num):
    # os.system(clear)
    print( num**2)
def sqrt(num):
    print( num**0.5)

def isPrime(num):
    # os.system(clear)
    flag = 0
    if (n == 0 or n == 1):
        flag = 1
    
def cube(num): 
    # os.system(clear)
    print(num**3)

def fact(num):
    # os.system(clear)
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    print(fact)

def choice(chose):
    
    number = int(input("Enter number to perform on: "))
    if(chose == 1):
        sqr(number)
    elif(chose == 2):
        sqrt(number)
    elif(chose == 3):
        cube(number)
    elif(chose == 4):
        fact(number)
    elif(chose == 5):
        primeFact(number)
    elif(chose == 6):
        isPrime(number)
    elif(chose == 7):
        print("Exiting....")
        exit(0)
    else:
        exit(0)
#initial
number = 0
def init():
    while(1): 
        print("""Welcome.
                Fuctions Available: 
                1. Find Squre
                2. Find Squareroot
                3. Find Cube
                4. Find Factorial
                5. Find Prime Factors
                6. Exit
                """)
        chose = int(input("\n choose a number: "))
        choice(chose)



init()
