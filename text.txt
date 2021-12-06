team = input()
name1 = input()
name2 = input()
name3 = input()
w=[name1, name2, name3]
e=""
for r in sorted(w):
    e = e + r + ", "
l = len(e)
k = e[:l-2]
print(f'{team}: {k}')
============    
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
m = max(x, y, z)
print(m)
===========
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
m = a/b
m = str(m)
l = len(m)
z = m[2:l]
c = c - 1
print(z[c])
=======
n = int(input())
p = n / 3
v = n / 3
k = n / 3
v += (p/2)+(k/2)
p = p/2
k = k/2
k+=(p/2)+(v/2)
v = v/2
p = p/2
p+=(k/2)+(v/2)
k = k/2
v = v/2
p = round(p)
v = round(v)
k = round(k)
print(p, v, k)
=========
[Провально]
n1 = int(input())
n1=math.fabs(n1)
r1 = n1
n2 = 0 
while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit
d1 = int(input())
d1 = math.fabs(d1)
r2 = d1
d2 = 0 
while d1 > 0:
    digit = d1 % 10
    d1 = d1 // 10
    d2 = d2 * 10
    d2 = d2 + digit
c = max(n2, d2)
if c == n2:
    c2 = n2 - r2
    print(round(c2))
elif c == d2:
    c2 = r1 + d2
    print(round(c2))
========
a, b = input().split()
result = []
for i in range(1):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    result.append(a == b)
if result[0] == True:
    print("Yes")
else:
    print("No")
======
num, base = input().split()
num = int(num)
base = int(base)
if not(2 <= base <= 9):
    pass
newNum = ''
while num > 0:
    newNum = str(num % base) + newNum
    num //= base
l = len(newNum) 
x = -1
z = 0
c = 1
for i in range(l):
    x += 1
    z = z + int(newNum[x])
    c = c * int(newNum[x])
print(c-z)
======
z, N = input().split()
z = int(z)
N = int(N)
x = []
for i in range(z, N) :
    a = str(i**2)     
    if a[-len(str(i))] == str(i) :
        x.append(i)
d = " ".join(map(str, x))
print(d)
======
n = int(input())
factors = []
d = 2
m = n
while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n//=d
        else:
            d += 1
factors.append(n)
print("*".join(map(str, factors))) 
=======
 n = int(input())
if n % 3 == 0:
    print("2")
else:
    print("1") 
=========
n, k = input().split()
n = int(n)
k = int(k)
result = 1 + (n-1) * k
for i in range(k-1):
    i+=1
    result += i * (n - 2)
print(result)

