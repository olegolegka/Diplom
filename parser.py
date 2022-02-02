import requests
from bs4 import BeautifulSoup
import csv
block_ulrs = []
for i in range(0,6,1):
    url = f"https://1teh.by/kompyuteryi-i-komplektuyuschie/kompyuternaya-tehnika/noutbuki/{i}"
    q = requests.get(url)
    result = q.content
    soup = BeautifulSoup(result, 'lxml')
    blocks = soup.find_all(class_ ="img-product-block" )

    print(blocks)
    for block in blocks:
        block_url = block.get('href')
        block_ulrs.append("https://1teh.by"+block_url)

with open('test.csv', 'w') as file:
    for line in block_ulrs:
        file.write(f'{line}\n')