a,b = list(map(int,input().split()))

def gcd(a,b):
    if a*b == 0:
        if a!=0:
            return a
        else:
            return b
    if a>b:
        return gcd(a%b,b)
    if a==b:
        return a
    return gcd(a,b%a)

print(gcd(a,b))
print((a//gcd(a,b))*(b//gcd(a,b))*gcd(a,b))