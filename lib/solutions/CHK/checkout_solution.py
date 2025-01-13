

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


def _build_checkout_basket(skus_array: list[str]) -> dict[str, int]:
    defaultdict()
    for sku in skus_array:
        if not is_valid_sku(sku):
            return None

        if len(sku) > 1:
            multiply = sku[:-1]
            item = sku[-1:]



def checkout(skus: str) -> int:
    total_price = 0
    skus_array = _build_skus_array(skus)

    basket = _build_checkout_basket(skus_array)
    for sku in skus_array:
        if not is_valid_sku(sku):
            return -1

        if len(sku) > 1:
            multiply = sku[:-1]
            item = sku[-1:]
            # offer = special_offers[item]
            # if offer:
            #     offer_units, offer_price = offer
            #     offer_multiply, regular_price_multiply = divmod(multiply, offer_units)
            #     total_price += (offer_multiply * offer_price)
            #     total_price += (item_prices[item] * regular_price_multiply)
            # else:
            #     total_price += item_prices[item]
        else:
            total_price += item_prices[sku]

    return total_price


def _build_skus_array(skus):
    i = 0
    skus_array = []
    current_sku = ''
    while i < len(skus):
        current_sku += skus[i]
        if not skus[i].isnumeric():
            skus_array.append(current_sku)
            current_sku = ''
        i += 1
    if current_sku:
        skus_array.append(current_sku)
    return skus_array


