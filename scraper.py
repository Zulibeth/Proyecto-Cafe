
import re
import requests
from bs4 import BeautifulSoup



def get_price_altura():
    url = "https://cafealtura.cl/productos/blend-de-la-casa-peru-brasil/"
    headers = {
            "User-Agent": "Mozilla/5.0"
        }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Busca el párrafo que contiene el rango de precio
    price_element = soup.select_one('p.price')
    precio_raw = price_element.text if price_element else "No disponible"
    precio_final = limpiar_precio(precio_raw)
    
    return precio_final

def limpiar_precio(precio_raw):
    if "Rango de precios" in precio_raw:
        return precio_raw.split("Rango de precios")[0].strip()
    return precio_raw.strip()



    
def get_price_mandrake():
    url = "https://cafemandrake.cl/products/blend-espresso-o-rei-da-praia-1kg"
    headers = {
                "User-Agent": "Mozilla/5.0"
            }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

        # Busca el párrafo que contiene el rango de precio
    price_element = soup.select_one('price-list')
    precio_raw = price_element.text if price_element else "No disponible"
    return limpiar_precio(precio_raw)
    


def limpiar_precio(precio_raw):
    # Buscar todos los patrones de precios tipo 10.900, $10.900, etc.
    precios = re.findall(r'\$?\d{1,3}(?:\.\d{3})+', precio_raw)

    if not precios:
        return "Precio no válido"

    # Si hay 2 o más precios, asumimos que es un rango
    if len(precios) >= 2:
        precio1 = precios[0] if precios[0].startswith('$') else f"${precios[0]}"
        precio2 = precios[1] if precios[1].startswith('$') else f"${precios[1]}"
        return f"{precio1} - {precio2}"

    # Si hay solo 1 precio, lo devolvemos formateado
    precio = precios[0]
    if not precio.startswith('$'):
        precio = f"${precio}"
    return precio




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




def get_all_prices():
    return {
        "Café Altura - Brasil Peru (250g)": get_price_altura(),
        "Café Mandrake - Blend Espresso (1kg)": get_price_mandrake(),
        "D'Lara - Blend Saphire El Salvador (250g)": get_price_dLara(),
    }
