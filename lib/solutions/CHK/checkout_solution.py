from collections import defaultdict
from typing import Optional

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


def _build_checkout_basket(skus_array: list[str]) -> Optional[dict[str, int]]:
    basket = defaultdict(int)
    for sku in skus_array:
        if not is_valid_sku(sku):
            return None

        if len(sku) > 1:
            multiply = int(sku[:-1])
            item = sku[-1:]
            basket[item] += multiply
        else:
            basket[sku] += 1

    return basket



def checkout(skus: str) -> int:
    total_price = 0
    skus_array = _build_skus_array(skus)
    basket = _build_checkout_basket(skus_array)
    if basket is None:
        return -1

    for item, item_count in basket.items():
        offer = special_offers[item]
        if offer:
            offer_units, offer_price = offer
            offer_multiply, regular_price_multiply = divmod(item_count, offer_units)
            total_price += (offer_multiply * offer_price)
            total_price += (item_prices[item] * regular_price_multiply)
        else:
            total_price += item_count * item_prices[item]

    return total_price


def _build_skus_array(skus: str) -> list[str]:
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