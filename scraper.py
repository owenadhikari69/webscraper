import requests
from bs4 import BeautifulSoup as soup 
my_url = "https://www.daraz.com.np/laptops/"
page = requests.get(my_url)
pagesrc = soup(page.text,'html.parser')
container = pagesrc.find('section',{'class':'products'})
gallary = container.find_all('div',{'class':'sku-gallery'})

f = open("Owen.csv" "w")
headers = "Brand,Model,Price"
f.write(headers)

#making a loop for galler for array data
for galleryitem in gallary{
    Model = gallaryitem.find('span'{'class':'name'}).gettext().strip()
    Brand + gallery.item.find('span',{'class':'brand'}).gettext().strip()
    price = galleryitem.find_all('span',{'class':'price'})[0].gettext().strip()

    f.write(Brand+","+Model+","+Price.replace("A")+"\n")
}