angka=998244353
def konvolusi(a,b):
    global angka
    x,y = len(a), len(b)
    c = [0] * (x+y-1)
    for i in range(x):
        for j in range(y):
            c[i+j] += (a[i] * b[j]) % angka
    for k in range(len(c)):
        c[k] %= angka
        print(c[k], end = " ")

a = [1, 2, 3, 4, 5]
b = [1, 1, 1]
konvolusi(a,b)