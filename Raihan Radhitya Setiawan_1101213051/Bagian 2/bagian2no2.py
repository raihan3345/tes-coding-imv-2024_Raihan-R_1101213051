fib = [0, 1] 

input= int(input('Masukkan Angka: '))

while fib[-1] <= input:
    fib.append(fib[-1] + fib[-2])

if input in fib:
    print(f'Angka {input} merupakan angka fibonacci.')
else:
    print(f'Angka {input} bukan angka fibonacci.')