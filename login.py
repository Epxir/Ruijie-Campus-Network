import re
from requests import get,post
from encrypt import encryptedPassword

def login(userId,password) :
   response = get('http://123.123.123.123/', verify=False, timeout=10)
   url = response.text.split('\'')[1]
   address = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', url)[0]
   queryString = url.split('?')[1]
   if len(password)!=256:
    password = encryptedPassword(password)
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
   return