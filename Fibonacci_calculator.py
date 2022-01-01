#Fibonacci calculator app
print("Welccome to finbonacci calcualtor app")
num=int(input("\nHow many digits of the fibonacci series would you like to compute: "))
#computeb the fibonacci series
fib=[1,1]
for i in range(num-2):
    new_fib=fib[i]+fib[i+1]
    fib.append(new_fib)

#display the series
print("\nThe first "+str(num)+" of the fibonacci sequence are:")
for number in fib:
    print(number)

#compute the golden ratio
golden=[]
for i in range(len(fib)-1):
    ratio=fib[i+1]/fib[i]
    golden.append(ratio)
#dislpay the ratio
print("\n The corresponding golden ratio are:")
for ratio in golden:
    print(ratio)
print("\n The ratio of consecutive  Fibonacci term approches phi; "+ str(1.618))
    
