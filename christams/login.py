import requests
from requests import Session

session = Session()
se_url = 'https://miloginci.michigan.gov/oidc/endpoint/default/token'
url = 'https://milogin.michigan.gov/eai/login/authenticate?URL=/'
url_session = 'https://miloginci.michigan.gov/v1.0/auth/session'
url_self = 'https://milogin.michigan.gov/uisecure/selfservice'
url_0xd = 'https://miloginci.michigan.gov/6etCh2/xPM/iXM/InybGZp6/QErYX6Nc/b3o0AQ/EU/0xdiEfRnEB'
url_bpk = 'https://s.go-mpulse.net/boomerang/QUF9E-G6ZRH-BKQBG-NXC6F-BBKP5'
url_enpoint = 'https://miloginci.michigan.gov/v1.0/endpoint/default/authorize?scope=openid%20profile%20email%20address%20phone%20groups&response_type=code&client_id=28d60358-8345-4827-9a4d-de796b4159c7&response_mode=form_post&redirect_uri=https://milogin.michigan.gov/pkmsoidc&state=42a4b775-4231-8dcf-804e-e488c397ba4d&nonce=c56b1ba9-47fd-2270-802b-a61c979a884f'
url_pkm_unkonw = 'https://milogin.michigan.gov/pkmsoidc?iss=&token=Unknown'
url_pkm = 'https://milogin.michigan.gov/pkmsoidc'
r = session.get(url)
body = {'grant_type': 'password', 'client_id': 'bf7d45a9-55f8-445b-a3a4-6c927d367caf', 'username': 'SfV1zLucj',
        'password': 'bA*eczpU'}
r2 = session.post(se_url, data=body)
print(r2.status_code, r2.json())
token = 'Bearer ' + r2.json()['access_token']
print(token)
header = {'authorization': token}
r3 = session.get(url_session, headers=header)
print('r3:',r3.status_code)
r4 = session.get(url_self)
print('r4:',r4.status_code)
r5 = session.get(url_pkm_unkonw)
print(r5.status_code,r5.text)

# r6 = session.get(url_enpoint)
# print('r6:',r6.status_code)
#
# r7 = session.get(url_0xd)
# print('r7:',r7.status_code)
#
# rbpk = session.get(url_bpk)

r8 = session.post(url_pkm)
print(r8.status_code)

r9 = session.get(url_self)
print(r9.text)
