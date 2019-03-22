import requests
from bs4 import BeautifulSoup as bs

# Two way for making Sessions
# 1 : s = requests.Session()
# 2 : with ~~

# with requests.Session() as s:
#     # HTTP GET Request : Use s instead of requests
#     req = s.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
#     # Get HTML SOURCE
#     html = req.text
#     # Get HTML Header
#     header = req.headers
#     # Get HTTP Status (normal : 200)
#     is_ok = req.ok


# Using with for arranging code
with requests.Session() as s:
    # HTTP GET Request : Use s instead of requests
    resp = s.get('https://www.naver.com/')
    print(resp)
    soup = bs(resp.content, 'html.parser')
    title = soup.select('div.view_title > div > h4 > span')
    contents = soup.select('#writeContents > p')

    print(title[0].text)
    for c in contents:
        print(c.text)
