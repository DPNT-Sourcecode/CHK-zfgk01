

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


def is_valid_sku(sku: str) -> bool:
    if len(sku) > 1:
        sku = sku[-1]

    return sku in item_prices.keys()


def checkout(skus: str) -> int:
    skus_array = skus.split()
    total_price = 0
    for sku in skus_array:
        if not is_valid_sku(sku):
            return -1

        if len(sku) > 1:
            multiply = sku[:-1]
            item = sku[-1:]
            offer = special_offers[item]
            if offer:
                offer_units, offer_price = offer
                offer_multiply, regular_price_multiply = divmod(multiply, offer_units)
                total_price += (offer_multiply * offer_price)
                total_price += (item_prices[item] * regular_price_multiply)
            else:
                total_price += item_prices[item]
        else:
            total_price += item_prices[item]

    return total_price
