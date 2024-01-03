from bs4 import BeautifulSoup
import requests
url='https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=82342659060&hvpone=&hvptwo=&hvadid=673584962059&hvpos=&hvnetw=g&hvrand=238383920730293008&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1011082&hvtargid=kwd-10573980&hydadcr=2246_13649807'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
print(soup)