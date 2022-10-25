def shopping_list(budget, **kwargs):
    basket = {}

    if budget < 100:
        return 'You do not have enough budget.'

    for k, v in kwargs.items():
        price, quantity = v[0], v[1]
        total = price * quantity

        if total <= budget:
            basket[k] = f'{total:.2f}'
            budget -= total

        if len(basket) == 5:
            return '\n'.join(f'You bought {k} for {v} leva.' for k, v in basket.items())

    return '\n'.join(f'You bought {k} for {v} leva.' for k, v in basket.items())


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))

print(shopping_list(20, jeans=(19.99, 1), ))

print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5), tomatoes=(4.20, 1),
                    milk=(2.50, 2), juice=(2, 3), eggs=(3, 1), ))
