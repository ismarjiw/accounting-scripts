"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    
    for melon_name, info in melons.items():
        print(melon_name)

        for key, value in info.items():
            print(f'{key} : {value}')

print_melon(melons)
