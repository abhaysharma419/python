from bs4 import BeautifulSoup as bs
import urllib.request as url
import requests
import os

url="https://www.pexels.com/"

html=requests.get(url)
c=html.text
page=bs(c,"html5lib")
article=page.findAll('article',{"class":"photo-item photo-item--overlay"})

# create directory for model images
if not os.path.exists('models'):
    os.makedirs('models')

# move to new directory
os.chdir('models')

# image file name variable
x = 0

for i in article:
    
    image=i.a.img['data-pin-media']
    response = requests.get(image)
    if response.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(image).content)
                f.close()
                x += 1
