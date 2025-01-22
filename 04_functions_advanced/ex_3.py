def sorting_cheeses(**kwargs):
    sorted_data = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""
    for cheese_name, quantity in sorted_data:
        result += cheese_name + "\n"
        # reversed(sorted(quantity))
        for el in sorted(quantity, reverse=True):
            result += f"{el}\n"
    return result[:-1]

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

# print(
#     sorting_cheeses(
#         Parmigiano=[165, 215],
#         Feta=[150, 515],
#         Brie=[150, 125]
#     )
# )



a = [2, 1, 4]
print(list(reversed((sorted(a)))))