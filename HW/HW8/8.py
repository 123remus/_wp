def is_prime(n):
    if n==1:
        return("it's not prime")
    for i in range(2,n):
        if n%i==0:
            return("it's not prime")
        else:
            return("it's prime")
print(is_prime(37))
print(is_prime(52))
print(is_prime(1))