import os
try:
 from uuid import uuid4 as uid
 from secrets import token_hex
 from OneClick import *
 import requests
except:
 os.system('pip install requests')
 os.system('pip install OneClick')
 os.system('pip install uuid')
 os.system('pip install secrets')
from uuid import uuid4 as uid
from secrets import token_hex
from OneClick import *
import requests
csr = token_hex(8)*2
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}==============================
|{G}[+] GitHub    : {B}whisper-666 |
|{G}[+] InstaGram : {B}_whisper.io_|
|{G}[+] TeleGram  : {B}whisper_io  |
{E}==============================''')
user=input(f'{S}[+] UserName ==> {B}')
print(f'{E}==============================')
head = {
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Host": "i.instagram.com",
      "Connection": "Keep-Alive",
      "User-Agent": Hunter.Services(),
      "Cookie": "mid=YwvCRAABAAEsZcmT0OGJdPu3iLUs; csrftoken="+csr,
      "Cookie2": "$Version=1",
      "Accept-Language": "en-US",
      "X-IG-Capabilities": "AQ==",
      "Accept-Encoding": "gzip",}
data= {"q":user,
   "device_id":f"android{uid}",
   "guid":uid,
   "_csrftoken":csr}
whisper=requests.post('https://i.instagram.com/api/v1/users/lookup/',headers=head,data=data).json()
email=whisper['obfuscated_email']
id=whisper['user']['pk']
prv=whisper['user']['is_private']
ph=whisper['has_valid_phone']
ce=whisper['can_email_reset']
sms=whisper['can_sms_reset']
fb=whisper['fb_login_option']
phn=whisper['phone_number']
wa=whisper['can_wa_reset']
lookup=f'''{G}[+] UserName ==> {user}
[+] UserID ==> {id}
[+] Is Private ==> {prv}
[+] E-mail ==> {email}
[+] Has Phone Number ? ==> {ph}
[+] E-mail Rest ==> {ce}
[+] SMS Rest ==> {sms}
[+] WhatsApp Rest ==> {wa}
[+] FaceBook Login ==> {fb}
[+] Phone Number ==> {phn}'''
print(lookup)
print(f'{E}==============================')
rest=input(f'{S}[+] Wanna Send Rest E-mail (Y/N) : {B}')
print(f'{E}==============================')
if rest == 'y' or rest == 'Y':
  data=data= {"user_email":user,
   "device_id":f"android{uid}",
   "guid":uid,
   "_csrftoken":csr}
  restt=requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',data=data,headers=head)
  res=restt.json()
  ress=restt.text
  if 'obfuscated_email' in ress:
   email=res['obfuscated_email']
   print(f'{G}[√] Done Send Rest : {B}{email}')
   print(f'{E}==============================')
  else:
   print(f'{E}[×] Error Send Rest')
   print(f'{E}==============================')
if rest == 'n' or rest == 'N':
 exit(f'{S}[÷] {B}tnak')
 print(f'{E}==============================')