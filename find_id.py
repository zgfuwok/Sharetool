from random import randint
import os
os.system('cls')
so_luong = input('NHẬP SỐ LƯỢNG: ')
for i in range(1,int(so_luong)):
    a = randint(100010000000000,100099999999999)
    print('SỐ LƯỢNG',i,end='\r')
    f = open('list-uid.txt','a+').write(str(a) + '\n')  