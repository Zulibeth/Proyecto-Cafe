
import requests
from bs4 import BeautifulSoup


    #PRUEBA 1
    # url = "https://cafealtura.cl/productos/blend-de-la-casa-peru-brasil/"
    # r = requests.get(url)
    # r.encoding = 'utf-8'
    # soup = BeautifulSoup(r.text, 'html.parser')

    # print(soup.prettify())

    # price = soup.select_one('p.price > span.woocommerce-Price-amount')
    # #return price.text if price else "No disponible"
    # if price:
    #     print("Elemento encontrado:", price)
    #     return price.text
    # else:
    #     print("Elemento no encontrado")
    #     return "No disponible"

    #PRUEBA 2
def get_price_altura():
    url = "https://cafealtura.cl/productos/blend-de-la-casa-peru-brasil/"
    headers = {
            "User-Agent": "Mozilla/5.0"
        }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Busca el párrafo que contiene el rango de precio
    price_element = soup.select_one('p.price')
    if price_element:
        return price_element.text.strip()
    return "Precio no disponible"
  


    #PRUEBA 1
    # url = "https://cafemandrake.com/product/blend-espresso-1kg/"
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text, 'html.parser')
    # price = soup.select_one('span.woocommerce-Price-amount')
    # return price.text if price else "No disponible"


    #PRUEBA 2 
def get_price_mandrake():
    url = "https://cafemandrake.cl/products/blend-espresso-o-rei-da-praia-1kg"
    headers = {
                "User-Agent": "Mozilla/5.0"
            }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

        # Busca el párrafo que contiene el rango de precio
    price_element = soup.select_one('price-list')
    if price_element:
        return price_element.text.strip()
    return "Precio no disponible"


# def get_price_58market():
#     url = "https://58market.cl/product/cafe-y-bebidas-en-polvo/sello-rojo-cafe-600gr"
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     price = soup.select_one('span.price') or soup.find('p', class_='price')
#     return price.text.strip() if price else "No disponible"


def get_price_dLara():
    url = "https://cafedlara.cl/collections/grano-molido/products/cafe-en-grano-y-molido-blend-saphire-el-salvador"
    headers = {
                "User-Agent": "Mozilla/5.0"
            }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

        # Busca el párrafo que contiene el rango de precio
    price_element = soup.select_one('span.current_price')
    if price_element:
        return price_element.text.strip()
    return "Precio no disponible"

print(get_price_dLara())
    #PRUEBA 2
    # try:
    #     url = "https://58market.cl/product/cafe-y-bebidas-en-polvo/sello-rojo-cafe-600gr"
    #     r = requests.get(url, timeout=10)
    #     soup = BeautifulSoup(r.text, 'html.parser')
    #     price = soup.select_one('span.price') or soup.find('p', class_='price')
    #     return price.text.strip() if price else "No disponible"
    # except Exception as e:
    #     print(f"Error al obtener precio de +58 Market: {e}")
    #     return "No disponible"





def get_all_prices():
    return {
        "Café Altura - Brasil Peru (250g)": get_price_altura(),
        "Café Mandrake - Blend Espresso (1kg)": get_price_mandrake(),
        "D'Lara - Blend Saphire El Salvador (250g)": get_price_dLara(),
    }
