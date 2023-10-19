import os,sys
import requests
import time
from time import strftime
os.system('cls')
find_file = input('NHẬP FILE CHỨA LIST UID: ')
find = open(find_file,'r',encoding='utf-8').read().split('\n')
print('CÓ ',len(find),'UID TRONG FILE')
o = 0
for get in find:
    o = o + 1
    r = requests.get('https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id='+get).text
    kq = print('LẦN',o,'|| UID:',get,'|| TIME:',strftime('%H:%M:%S'),'|| STATUS:',r)
