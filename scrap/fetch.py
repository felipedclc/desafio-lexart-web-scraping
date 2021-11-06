from parsel import Selector
import requests
import time


# URL_BASE = "https://www.buscape.com.br"


def get_url_products_buscape(produto):
    """Obtem a url da página com os produtos buscados"""
    return f"https://www.buscape.com.br/search?q={produto}"


def fetch(url):
    """Faz uma requisição HTTP e retorna o conteúdo HTML da resposta."""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        response.raise_for_status()
        return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


def scrape_buscape(html_content):
    """Busca informações do conteudo e preenche um dicionário com atributos"""

    selector = Selector(html_content)

    titles = selector.css(
        "h2.Text_Text___RzD-.Text_LabelSmRegular__2Lr6I::text"
    ).getall()
    imgs = selector.css("img.Cell_Image__2-Jrs::attr(srcset)").getall()
    prices = selector.css(".CellPrice_MainValue__3s0iP::text").getall()
    categories = selector.css(
        "a.Breadcrumb_Link__nn-YI.breadcrumb-link::attr(href)"
    ).getall()[1]
    links = selector.css(".Cell_CellBody__3XC7o > a::attr(href)").getall()

    products = []
    for index in range(len(titles)):
        dictionary = {
            "thumbnail": imgs[index].split("640w")[0].strip(),
            "title": titles[index],
            "price": float(
                prices[index]
                .split("R$")[1]
                .strip()
                .replace(".", "")
                .replace(",", ".")
            ),
            "category_id": categories.split("/")[1],
            "permalink": "https://www.buscape.com.br" + links[index],
        }
        products.append(dictionary)

    return products


def scrape_next_page_link(html_content):
    """Faz o scrape do HTML e obtem a URL da próxima página."""
    selector = Selector(html_content)
    next_page_url = "&page=1"
    while next_page_url:
        next_page_url = selector.css(
            "a.Paginator_pageLink__v3t86::attr(href)"
        ).get()
        return next_page_url


# print(scrape_buscape(fetch(get_url_products_buscape("macbook"))))
