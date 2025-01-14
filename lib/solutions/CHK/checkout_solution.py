from collections import defaultdict
from typing import Optional

# noinspection PyUnusedLocal
# skus = unicode string
item_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}


special_offers = {
    'A': [(3, 130), (5, 200)],
    'B': [(2, 45)],
    'E': [(2, '-1B')]
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

    for item, item_count in basket.items():
        best_offer = _get_best_offer(item, item_count)

        while item_count > 0 and item_count >= best_offer[0]:
            best_offer = _get_best_offer(item, item_count)
            offer_units, on_offer = best_offer
            if offer_units and item_count >= offer_units:
                if not isinstance(on_offer, int):  # free items offer
                    free_item, quantity = on_offer[-1:], int(on_offer[1:-1])
                    if item_count >= offer_units and basket.get(free_item): # is eligible for free items
                        quantity_to_deduct = min(quantity, basket.get(free_item, 0))
                        basket[free_item] -= quantity_to_deduct
            else:
                break
            item_count = item_count - offer_units
            best_offer = (0, 0)
    print(basket)
    return basket


def _get_best_offer(item, item_count):
    best_offer = (0, 0)
    offers = special_offers.get(item, [])
    for offer in offers:
        offer_units, on_offer = offer
        # choosing the best offer based on quantity
        if best_offer[0] <= offer_units <= item_count:
            best_offer = offer
    return best_offer


def checkout(skus: str) -> int:
    total_price = 0
    skus_array = _build_skus_array(skus)
    basket = _build_checkout_basket(skus_array)
    if basket is None:
        return -1

    for item, item_count in basket.items():
        offers = special_offers.get(item, [])
        best_offer = _get_best_offer(item, item_count)
        if offers:
            while item_count > 0 and item_count >= best_offer[0]:
                offer_units, on_offer = best_offer
                if offer_units and item_count >= offer_units:
                    if isinstance(on_offer, int):
                        # x items for n price
                        total_price += on_offer
                    else:  # free items offer
                        if item_count >= offer_units: # is eligible for free items
                            total_price += offer_units * item_prices[item]
                else:
                    break
                item_count = item_count - offer_units
                best_offer = _get_best_offer(item, item_count)

            total_price += item_count * item_prices[item]
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


if __name__ == '__main__':
    print(checkout('AABBCCDDEE'))