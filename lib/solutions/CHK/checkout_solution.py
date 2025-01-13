

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

special_offers = {
    'A': (3, 130),
    'B': (2, 45),
}
def checkout(skus: str) -> int:
    skus_array = skus.split()
    total_price = 0
    for sku in skus_array:
        multiply = sku[:-1]
        item = sku[-1:]
        if multiply:
            offer = special_offers[item]
            if offer:
                offer_units, offer_price = offer
                


