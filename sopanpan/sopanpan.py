# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup as bs
import urllib.request
requests.packages.urllib3.disable_warnings()


headers = {
    "Host": "www.sopanpan.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.sopanpan.com/search/%E6%9D%83%E5%8A%9B%E7%9A%84%E6%B8%B8%E6%88%8F-0-0.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "sopanpanwx=1; Hm_lvt_413b8e292048b1753606d3b7576446f3=1516524882,1516604831,1517397120,1517453196; UM_distinctid=1614f423d7a5a-0ccf90e409e982-4323461-1fa400-1614f423d7b1c1; Hm_lvt_66be306d99cad41c78b42980eb034651=1517453202; Hm_lpvt_66be306d99cad41c78b42980eb034651=1517453202; Hm_lpvt_413b8e292048b1753606d3b7576446f3=1517453238; CNZZDATA1261677980=799337431-1517453195-%7C1517453237; Hm_lvt_cb48bb397e3ec124a1cf1cee84008840=1516524899,1516604844,1517397158,1517453239; Hm_lpvt_cb48bb397e3ec124a1cf1cee84008840=1517453239"
}


def inputprocess(name):
    name = "zt/" + name
    return urllib.request.quote(name)


def urlprocess(proname,linklist):
    url = "https://www.sopanpan.com/" + proname
    r = requests.get(url, headers=headers, verify=False)
    text = r.text
    soup = bs(text, "html.parser")
    ulst1 = soup.find("div", class_="ulst1")
    # 获取链接
    try:
        spans = ulst1.find_all('span', class_="_l")
    except :
        return 0
    
    for span in spans:
        a = span.find('a')
        if (a):
            link = a['href']
            newlink = "https://www.sopanpan.com" + link
            linklist.append(newlink)
        else:
            pass
    try:
        next_page = soup.find("td", class_="next")
    except:
        pass
    else:
        if(next_page):
            newpagelink = next_page.find('a')['href']
            newpagelink = newpagelink.replace('/zt/', 'zt/')
            urlprocess(newpagelink,linklist)


