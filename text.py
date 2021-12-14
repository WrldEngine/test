n, m = input().split()
n = int(n)
m = int(m)
x = 0
x1 = 0
r = 1
for i in range(n):
    i += 1
    i = i % m 
    x = x + i
    r += 1
    r = m % r
    x1 = x1 + r
print(x1+x)
=====
n = int(input())
m = []
for i in range(n):
    i+=1
    if n % i == 0:
        m.append(n/i)
z = list(set(m))
m = len(z)
print(m) 
=====
N = int(input())
if N % 3 == 0:
    print("2")
if N % 3 == 1:
    print("1")
    print("1")
if N % 3 == 2:
    print("1")
    print("2")
=====
a, b = input().split()
c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if b < a:
    t = b 
    b = a 
    a = t
if c >= d:
    t = c
    c = d 
else:
    t = d 
d2 = (t**2)+(d**2)
if (d <= a and t <= b or (a * math.sqrt(d2 - (b * b)) + b * math.sqrt(d2 - (a * a))) <= (t * t) - (c * c)):
    print("Possible")
else:
    print("Impossible")
=====
n = int(input())
z = 0
m = 0
if n > 1:
    for i in range(n):
        a, b, c, d = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        AREA = math.fabs(c - a) * math.fabs(d - b)
        m = AREA
        z = m - (1/4) * AREA
        AREA += z
if n == 1:
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    AREA = math.fabs(c - a) * math.fabs(d - b)
print(round(AREA))
====
n = int(input())
if n % 2 == 0:
    n = n // 2
    b = n * "B"
    r = n * "R"
    print(b+r)
    exit()

if n % 2 == 1:
    n+=1
    n = n // 2
    b = n * "B"
    r = n * "R"
    m = b+r
    l = len(m)
    print(m[0:l-1])
====
n = int(input())
z = 0
l = 0
for i in range(n):
    z += 1
    m = math.factorial(z)
    l += m 
print(l)
=====
n = int(input())
if n == 1:
    print("1")
if n % 3 == 0:
    d  = n/3
    s = pow(3, d)
if n % 3 == 2:
    d = n/3
    s = 3 ** d
if n % 3 == 1:
    n = n - 4
    d = n/3
    s = pow(3, d)
    s = s * 4
print(round(s))
=====
n = int(input())
res = 0
all_date = [0] * (n+1)
if n != 0 and not(n % 2):
    all_date[0] = 1
    all_date[2] = 3
    if n > 2:
        all_date[4] = 11
    for i in range(6, n+1, 2):
        all_date[i] = 4 *all_date[i-2] - all_date[i-4]
    
    res = all_date[n]
print(res) 
====
n, k = input().split()
n = int(n)
k = int(k)
result = 1 + (n-1) * k
for i in range(k-1):
    i+=1
    result += i * (n - 2)
print(result)
====
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

