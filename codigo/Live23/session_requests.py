from requests import Session

s = Session()
s.get('http://google.com')
print(s.cookies)
s.get('http://facebook.com')
print(s.cookies)
