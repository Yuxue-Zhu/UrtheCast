def Fib(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fib(n-1) + Fib(n-2))  
  
def main():
    n = int(input("Enter the terms? "))  # take input from the user
  
    if n <= 0:  # check if the number is valid 
        print("Please enter a positive integer")  
    else:  
        print("Fibonacci sequence:")  
    
        print(Fib(n))

if __name__ == "__main__":
    main()