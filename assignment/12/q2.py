# Write a python script to check whether a given number is Prime or not
prime_num= int(input("Enter the number you wish to chick is it prime or not : "))
if prime_num>1:
    for i in range(2,int(prime_num/2),1):
        if( prime_num%i==0):
            print(f" the enteed number {prime_num} is not prime")
            break
    else:
        print(f" the enteed number {prime_num} is prime")
if prime_num<0:
    for i in range(-2,int(prime_num/2),-1):
        if(prime_num%i==0):
            print("not prime")
            break
    else:
        print("prime")
# else:
#     print(f" the enteed number {prime_num} is not prime")

# else:
#     print("not prime")