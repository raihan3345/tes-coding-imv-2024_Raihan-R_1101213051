lebar = 7
  
for i in range(lebar):
  for j in range(lebar-i):
    print(' ',end='')
      
  for k in range(i+1):
    print('* ',end='')
  print()
 
for i in range(1,lebar):
  for j in range(i+1):
    print(' ',end='')
      
  for k in range(lebar-i):
    print('* ',end='')
  print()