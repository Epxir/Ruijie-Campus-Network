import re
from requests import get,post
from encrypt import encryptedPassword
from urllib.parse import urlparse,parse_qs

def login(userId,password) :
   response = get('http://123.123.123.123/', verify=False)
   url = response.text.split('\'')[1]
   address = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)[0]
   queryString = url.split('?')[1]
   if len(password)!=256:
    macStringTemp=parse_qs(urlparse(url).query).get('mac')[0]
    password = encryptedPassword(address,macStringTemp,password,queryString)
   params = {
       'method': 'login',
   }
   
   data = {
       'userId': userId,
       'password': password,
       'service': '',
       'queryString': queryString,
       'operatorPwd': '',
       'operatorUserId': '',
       'validcode': '',
       'passwordEncrypt': 'true',
   }
   
   response = post(
       address+'/eportal/InterFace.do',
       params=params,
       data=data,
       verify=False,
   )
   print(response.text)
   return