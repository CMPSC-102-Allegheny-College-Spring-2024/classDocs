#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Application 6: Online Shopping Cart with Discounts using Sets")

# Items in the shopping cart
shopping_cart = {'Laptop', 'Headphones', 'Mouse', 'Backpack', 'Laptop', 'Mouse'}

# Available discounts
discounted_items = {'Mouse', 'Backpack'}

# Apply discounts to the shopping cart
discounted_cart = shopping_cart - discounted_items

# Display results
print(f"Original Shopping Cart: {shopping_cart}")
print(f"Discounted Items: {discounted_items}")
print(f"Final Cart after Discounts: {discounted_cart}")
