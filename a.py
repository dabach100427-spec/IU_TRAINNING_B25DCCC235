'''#if5-rẽ nhánh 5
import math
n=int(input())
print("YES" if (math.sqrt(n))**2==n and n>=0 else "NO")
#if6-rẽ nhánh 6
a,b,c= map(int, input().split())
if a+b>c and a+c>b and b+c>a:
    print("YES")
else:
    print("NO")
#if7-rẽ nhánh 7
a,b,c=map(int, input().split())
d=b**2-4*a*c
if d<0:
    print("NOSOL")
elif d==0:
    print("ONE")
else:
    print("TWO")'''
#LOOP4 - Vòng lặp while 4
n=int(input())
if 0<n<=1000:
    i=0
    while i<n:
        j=0
        while j<i:
            print("$", end="")
            j+=1
        print()
        i+=1
else:
    print("input error")

