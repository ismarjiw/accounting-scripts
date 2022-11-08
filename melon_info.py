"""Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness, melon_flesh_color, melon_rind_color, average_weight


def print_melon(name, price, seedless, flesh, rind, weight):
    """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])

for i in melon_names:
    name = melon_names[i]

for i in melon_prices:
    price = melon_prices[i]

for i in melon_seedlessness:
    seedless = melon_seedlessness[i]

for i in melon_flesh_color:
    flesh = melon_flesh_color[i]

for i in melon_rind_color:
    rind = melon_prices[i]

for i in average_weight:
    weight = average_weight[i]

