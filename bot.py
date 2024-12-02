import random,os,time
import requests,sys
from rich import print
from rich.prompt import Prompt
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.exceptions import ProxyError, ConnectTimeout, ReadTimeout, RequestException
os.system('clear')
print("""
[green]┌─────────────── [white bold]info [/white bold][green]────────────────┐
[green]│[white italic] Devoloper [/white italic]:[white italic] Saifur Rahman Siam      [/white italic][green]│
[green]│[white italic] Youtube   [/white italic]:[white italic] Noob Programmer (nbprg) [/italic white][green]│
[green]│[white italic] Telegram  [/white italic]:[white italic] @TataCuto (CR7)         [/italic white][green]│
[green]│[white italic] ToolsType [/white italic]:[white italic] Pipecdn point collect   [/italic white][green]│
[green]└─────────────────────────────────────┘
""".strip()
)
def angle(a):
   if a == 'a':return '┘'
   elif a == 'b':return '┐'
   elif a == 'c':return '┌'
   elif a == 'd':return '└'
def login_pipe():
    print('[italic white] Login Pipe Guardian Account[resset all]')
    email, password = Prompt.ask(f'   {angle("d")}───[green italic] Mail \033[0;32m'), Prompt.ask('   └───[green italic] Password ')
    url = 'https://pipe-network-backend.pipecanary.workers.dev/api/login'
    head = {"Content-Type": "application/json" }
    json_data = {'email': email,'password': password}
    try:
        response = requests.post(url,headers=head,json=json_data).json()
        token = response['token']
        print('   └───[green italic] Login Successful')
        return token
    except:
         print('   └───[red italic] Failed to login ')
         exit()
def chack_point(token):
   try:
     head = {'Authorization': f'Bearer {token}'}
     url = 'https://pipe-network-backend.pipecanary.workers.dev/api/points'
     response = requests.post(url,headers=head).json()
     return response['points']
   except:
      return '°-°'
def view_nodes(proxy):
    try:
       response = requests.get('https://pipe-network-backend.pipecanary.workers.dev/api/nodes',proxies=proxy).json()
       return response['node_id']
    except:
      return 'Error Get Nodes '
def send_hartbeat():
    url = 'https://pipe-network-backend.pipecanary.workers.dev/api/heartbeat'
    head = {"Authorization": f"Bearer {token}",
        "Content-Type": "application/json"}
    json_data = {'username': username, 'ip': ip, 'geo': geo}
    response = requests.post(url,headers=head,json=json_data).json()
    return response
def httpx(proxy):
     res = requests.get('http://ip-api.com/json').json()
     return res
point=0
def get_one_points(proxy,token):
    global point
    sys.stdout.write(f'\r\033[0m   └───\033[0;32m Request points\033[0m :\033[0m {point} ');sys.stdout.flush()
    try:
          proxyx = {'http': proxy,
          'https': proxy}
          headers = {
          'authorization': f'Bearer {token}',
          'content-type': 'application/json',
          }
          try:
             ip = proxy.split('@')[1].split(':')[0]
          except:
             ip = proxy.split(':')[0]
          json_data = { 'node_id': f"{str(random.choice(['1','2','3','4','5','6','7','8','9','10']))}",
          'ip': ip, 'latency': int(random.randint(170,1243)),
          'status': 'online',
          }
          response = requests.post('https://pipe-network-backend.pipecanary.workers.dev/api/test',headers=headers,json=json_data,proxies=proxyx,timeout=5).json()
          point+=int(response['points'])
    except Exception as e:
          sys.stdout.write(f'\r\033[0m   └───\033[0;31m Request Point Error ');sys.stdout.flush()
try:proxy_list=open('proxy.txt','r').read().splitlines()
except:print('[red]proxy file not found')
"""
http,socks4,socks5 = 0,0,0
for item in proxy_list:
    if 'socks4:/' in item:socks4+=1
    elif 'http://' in item:http+=1
    elif 'socks5://' in item:socks5+=1

print(f'[italic white] Total Proxy List Count[resset all]')
print(f'   └───[green italic] Total http Proxy   [/green italic]:',http)
print(f'   └───[green italic] Total socks4 Proxy [/green italic]:',socks4)
print(f'   └───[green italic] Total socks5 Proxy [/green italic]:',socks5);print('')
"""
token = login_pipe()
print('');print(f'[italic white] Accaunt Tatal Balance Now : {chack_point(token)}[resset all]')
def main(proxy_list,token):
    results = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        future_to_proxy = {executor.submit(get_one_points, proxy, token): proxy for proxy in proxy_list}
        for future in as_completed(future_to_proxy):
            result = future.result()
            results.append(result)
    return results

while True:main(proxy_list,token)
