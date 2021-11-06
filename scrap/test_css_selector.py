""" from parsel import Selector
import requests

URL_BASE_1 = "https://www.buscape.com.br/search?q=macbook"

response = requests.get(URL_BASE_1).text

selector = Selector(response)

titles = selector.css("h2.Text_Text___RzD-.Text_LabelSmRegular__2Lr6I::text").getall()
imgs = selector.css("img.Cell_Image__2-Jrs::attr(srcset)").getall()
prices = selector.css(".CellPrice_MainValue__3s0iP::text").getall()
categories = selector.css("a.Breadcrumb_Link__nn-YI.breadcrumb-link::attr(href)").getall()[1]
links = selector.css(".Cell_CellBody__3XC7o > a::attr(href)").getall()

for title in titles:
    print({"title": title}) """

""" for img in imgs:
    print({"thumbnail": img.split("640w")[0].strip()}) """

""" for price in prices:
    print({"price": float(price.split("R$")[1].strip().replace(".", "").replace(",", "."))})
 """

""" for link in links:
    print({"link": "https://www.buscape.com.br" + link})

products = []
for index in range(len(titles)):
    dictionary = {
        "thumbnail": imgs[index].split("640w")[0].strip(),
        "title": titles[index],
        "price": float(prices[index].split("R$")[1].strip().replace(".", "").replace(",", ".")),
        "category_id": categories.split("/")[1],
        "permalink": "https://www.buscape.com.br" + links[index]
    }
    products.append(dictionary)

print(products)
 """
