from bs4 import BeautifulSoup
import requests

host = "brd.superproxy.io:22225"
user_name = "brd-customer-hl_88bbc072-zone-my_unlocker"
password = "m4lgw4h4cn0w"
proxy_url = f"https://{user_name}:{password}@{host}"

proxies = {"http": proxy_url, "https": proxy_url}

print(proxy_url)

url = "https://eomisae.co.kr/os"

response = requests.get(url, proxies=proxies, verify=False)
html = response.text
print(html)