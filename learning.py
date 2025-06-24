def apply_discount_and_tax(price):
    discounted_item = [round(item * 0.9, 2) for item in price]
    item_after_tax = [round(item * 1.21, 2) for item in discounted_item]

    return discounted_item, item_after_tax

def print_invoice(items):
    discounted_items, items_after_tax = apply_discount_and_tax(items)
    for i, item in enumerate(items):
        print(f"Item {i+1}: Original price €{item:.2f} -> Discounted price: €{discounted_items[i]:.2f} -> With tax: €{items_after_tax[i]:.2f}")

print_invoice([10,20,30,40])