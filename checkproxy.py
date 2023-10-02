import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor
from pystyle import System
mdo = '\u001b[31;1m'
mxanh = '\u001b[32;1m'
blue = '\u001b[34;1m'
mvang = '\u001b[33;1m'
mtrang = '\u001b[0m'
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import requests
import socket
from pystyle import *
#import màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
#Đánh Dấu Bản Quyền
LCT_tool = trang + "~" + trang + "[" + do + "+" + trang + "] " + trang + "=> "
toandz = trang + "~" + trang + "[" + do + "÷" + trang + "] " + trang + "=> "
thanh = trang + "-------------------------------------------------------------------------"
#today nand clear
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
def logo():
    os.system("cls" if os.name == "nt" else "clear")
    logo=f"""
\033[1;33m███████╗███████╗██╗    ██╗   ████████╗██╗   ██╗███╗   ██╗
\033[1;32m╚══███╔╝██╔════╝██║    ██║   ╚══██╔══╝██║   ██║████╗  ██║
\033[1;34m  ███╔╝ █████╗  ██║ █╗ ██║█████╗██║   ██║   ██║██╔██╗ ██║
\033[1;36m ███╔╝  ██╔══╝  ██║███╗██║╚════╝██║   ██║   ██║██║╚██╗██║
\033[1;31m███████╗██║     ╚███╔███╔╝      ██║   ╚██████╔╝██║ ╚████║
\033[1;30m╚══════╝╚═╝      ╚══╝╚══╝       ╚═╝    ╚═════╝ ╚═╝  ╚═══╝                                                         
\033[1;37m        Devoloper: Dươngg Phú Quốcc | Version: 1.0
\033[1;33m─────────────────────────────────────────────────────────────────────────────
\033[1;31m~ [♪] ✅✅ \033[1;34mAdmin: \033[1;36mDươngg Phú Quốcc ✅
\033[1;31m~ [♪] ✅✅ \033[1;35mFacebook: \033[1;34mhttps://www.facebook.com/User.Quoc509
\033[1;31m~ [♪] ✅✅ \033[1;32mTikTok: \033[1;35mhttp://www.TikTok.com/@Wok.509
\033[1;31m~ [♪] ✅✅ \033[1;30mYoutube: \033[1;37mhttp://www.Youtube.com/@WokLamTool
\033[1;33m─────────────────────────────────────────────────────────────────────────────
\033[1;31m~ [%] ✅✅ \033[1;36m01/01/2024 - \033[1;37mKhông Có Vấn Đề, Mọi Thứ Ổn
\033[1;33m─────────────────────────────────────────────────────────────────────────────
{a}{luc}~ [&] ✅✅ \033[1;36mYOUR IP: {ip}\033[1;31m
  """
    print(logo)
#=======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
logo()
with open('live.txt','w') as file1:
    file1.write('Tool Check Proxy_Live[Jusst]\n')
def check_proxy(proxy):
    
    proxy = proxy.strip()
    url = f'https://clonebysun.com/api/tienich/checkliveproxy/{proxy.strip()}'
    data = requests.get(url)
    if 'ip' in data.json() and 'proxy' in data.json() and 'status' in data.json():
        country = data.json()["country"]
        if data.json()['ip'] != 'error' and data.json()['proxy'] != '' and data.json()['status'] != 'Die':
            print(f'{mxanh}Live => {data.json()["ip"]} {blue}Country {mvang}{data.json()["country"]} ')
            with open('live.txt', 'a+') as f:
                f.write(proxy + " | "+country+"\n")
        else:
            print(f'{mdo}Die => {mtrang}{proxy}')
    else:
        print(f'{mdo}Invalid JSON response: {data.text}')
    
file_path = input(f'{mtrang}Nhập đường dẫn file cần kiểm tra: {mvang}')
if not os.path.exists(file_path):
    print(f'{mdo}Lỗi: File không tồn tại')
    exit()

# Đọc dòng từ file
with open(file_path, 'r') as file:
    lines = file.readlines()
luong=int(input("Nhập Số Luồng: "))
# Sử dụng ThreadPoolExecutor với 10 luồng để kiểm tra nhanh hơn
with ThreadPoolExecutor(max_workers=luong) as executor:
    # Chạy các nhiệm vụ kiểm tra proxy đa luồng
    executor.map(check_proxy, lines)
print(f'{mvang}Hoàn tất, kết quả đã được lưu vào file: {mxanh}live.txt')