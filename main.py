import requests
from bs4 import BeautifulSoup as BS

def println(a):
    print ('\n' * a)

product = input("Product name:")


my_amazon_url ="https://www.amazon.in/s?k="+product+"&qid=1594752790&ref=sr_pg_2"

my_flipkart_url = "https://www.flipkart.com/search?q="+product+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

def call(my_url,b):
    r = requests.get(my_url)
    page_html = r.text
    #---------------------------------------

    soup = BS(page_html,'html.parser')
    print(soup.title.string)

    println(3)

    # for i in soup.body.descendants:
    #     if i.name == None:
    #         print(i)
    #     else:
    #         print(i.name)


    # for link in soup.find_all('a'):
    #     href = link.get("href")
    #     if "twitter" in href:
    #         print(href)

    for i in soup.find_all('div',{'class':b}):
        print(i.text)


call(my_flipkart_url,'_1vC4OE')
call(my_amazon_url,"a-price-whole")
