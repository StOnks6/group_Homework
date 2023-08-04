from typing import Dict, List


def get_affordable_products(products: List[Dict[str, int]], max_price: int) -> list[int]:
    affordable_products = []
    for product in products:
        if product['price'] <= max_price:
            affordable_products.append(product['product'])
    return affordable_products
