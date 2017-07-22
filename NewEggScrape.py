from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

myUrl='https://www.newegg.com/Product/ProductList.aspx?Submit=Property&N=100007709%2050001402%2050001312%2050001315%2050001561%2050001314%2050001669%2050001419%2050012150%2050001471%20600487565%20600487564%20600565503%20600582123%20600565502%20601206485%204814%20601206353%20601273503%20601273511&IsNodeId=1&bop=And&PageSize=60&order=PRICE'

uClient = uReq(myUrl)

pageHTML = uClient.read() 
uClient.close()

filename = "products.csv"
headers = "brand, product_name, shipping\n"
f = open(filename, "w")
f.write(headers)


page_soup = soup(pageHTML, "html.parser")
containers = page_soup.findAll("div", {"class" : "item-container"})

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    shipping_items = container.findAll("li", {"class":"price-ship"})
    shipping_fee = shipping_items[0].text.strip()

    f.write(brand + "," + product_name.replace(",","|") + "," + shipping_fee + "\n")

f.close()

print('The scrape has completed')

