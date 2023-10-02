from datetime import datetime
import time,os,sys,json,random
from threading import Thread
try:
	import requests
except:
	os.system('pip install requests')
	import requests


dem = 0
list_pic = []
xanh_la = "\033[1;32m"
xanh_duong = "\033[1;34m"
do = "\033[1;31m"
vang = "\033[1;33m"
trang = "\033[1;37m"
tim = "\033[1;35m"
nminh = "</>"

def logo():
    banner = f"""
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
\033[1;33m─────────────────────────────────────────────────────────────────────────────\033[1;32m"""
    print(banner)


def avatar(fb_dtsg,jazoest,cookie,id_reg,name):
	headers = {
		'cookie': cookie,
		'referer': 'https://www.facebook.com/pages/creation/?ref_type=launch_point',
		'sec-ch-prefers-color-scheme': 'light',
		'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
		'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.120", "Chromium";v="109.0.5414.120"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-ch-ua-platform-version': '"0.1.0"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
		'x-asbd-id': '198387',
		'x-fb-friendly-name': 'AdditionalProfilePlusEditMutation',
		'x-fb-lsd': 'VvOG1zo3ie0zBti8fQ6zUf'
	}
	data = {
		'fb_dtsg': fb_dtsg,
		'jazoest': jazoest,
		'fb_api_caller_class': 'RelayModern',
		'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
		'variables': '{"input":{"bio":"AUTO REG PAGE BY ZFW","categories":["1062586164506537"],"creation_source":"comet","name":"%s","page_referrer":"launch_point","actor_id":"100037533160611","client_mutation_id":"2"}}' %(name),
		'server_timestamps': 'true',
		'doc_id': '5296879960418435'
	}
	a = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
	try:
		id = a['data']['additional_profile_plus_create']['additional_profile']['id']
		print(f'{tim}{datetime.now().strftime("%H:%M:%S")} : DUONGG_PHU_QUOCC : ID PROFILE : {id} : NAME PROFILE : {name} ')
		time.sleep(8)
		id_pic = random.choice(list_pic)
		headers = {
			'cookie':f'{cookie} i_user={id} ;',
			'referer': f'https://www.facebook.com/profile.php?id={id}',
			'sec-ch-prefers-color-scheme': 'light',
			'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
			'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Google Chrome";v="109.0.5414.132", "Chromium";v="109.0.5414.132"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-ch-ua-platform-version': '"0.1.0"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
			'x-asbd-id': '198387',
			'x-fb-friendly-name': 'ProfileCometProfilePictureSetMutation',
			'x-fb-lsd': 'Gjs2V-dxZJaWc-rXs6xTfk',
		}
		data = {
			'fb_dtsg': fb_dtsg,
			'jazoest': jazoest,
			'fb_api_caller_class': 'RelayModern',
			'fb_api_req_friendly_name': 'ProfileCometProfilePictureSetMutation',
			'variables':'{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1689243911841,773058,190055527696468,;ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1689243900861,329582,250100865708545,","caption":"add url : https://www.facebook.com/100002492272111 (Nguyễn Minh)","existing_photo_id":"%s","expiration_time":null,"profile_id":"%s","profile_pic_method":"EXISTING","profile_pic_source":"TIMELINE","scaled_crop_rect":{"height":0.99999,"width":0.99269,"x":0.00365,"y":0.00001},"skip_cropping":true,"actor_id":"%s","client_mutation_id":"1"},"isPage":false,"isProfile":true,"sectionToken":"UNKNOWN","collectionToken":"UNKNOWN","scale":1}' %(id_pic,id,id),
			'server_timestamps': 'true',
			'doc_id': '5399282646840954'
		}
		avatar = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
		print(f'{datetime.now().strftime("%H:%M:%S")} : DUONGG_PHU_QUOCC : AVATAR SUCCESS : {id} ')
	except:
		print(f'{datetime.now().strftime("%H:%M:%S")} : DUONGG_PHU_QUOCC : {id_reg} : REG PAGE FALSE ')

	
logo()
cookie = input('COOKIE FACEBOOK CẦN REG: ')
print('-'*60)

while True:
	try:
		so_luong = int(input('SAU BAO LẦN REG THÌ DỪNG TOOL : '))
		break
	except:
		print('VUI LÒNG NHẬP SỐ LẦN REG ')

print('-'*60)

while True:
	try:
		id_pict = input('ID ẢNH ( CÓ THỂ THÊM NHIỀU ẢNH ): ')
		list_pic.append(id_pict)
		if id_pict == "":
			break
	except:
		break

print('-'*60)

while True:
	try:
		delay = int(input('DELAY GIỮA CÁC LẦN REG : '))
		break
	except:
		print('VUI LÒNG NHẬP DELAY ')

print('-'*60)


os.system("cls" if os.name == "nt" else "clear")


while dem < so_luong:
	try:
		id_reg = cookie.split('c_user=')[1].split(';')[0]
		find_data = requests.get(f"https://mbasic.facebook.com/profile.php?id={id_reg}", headers={'cookie':cookie}).text
		fb_dtsg = find_data.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
		jazoest = find_data.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
		name_fb = find_data.split('<title>')[1].split('</title>')[0]
		print(f'ID : {id_reg} || NAME : {name_fb}')
		name = requests.get('https://bossylankydictionary--minhnguyen628.repl.co/name.php').json()['name']
		avatar(fb_dtsg,jazoest,cookie,id_reg,name)
		time.sleep(3)
		dem += 1
		if dem == so_luong:
			print('HOÀN THÀNH REG ! ')
			break
			quit()
	except:
		print(f"Cookie {cookie} Die Vui Lòng Kiểm Tra Lại!!! ")
		quit()
	time.sleep(delay)