# Sets

utensils = {"fork", "knife", "spoon", "spatula"}
print(utensils, type(utensils))

utensils.add("garlic press")
print(utensils)
utensils.add("spoon")
print(utensils)
utensils.discard("knife")
print(utensils)

# An unordered, unique collection

rep_list = [1, 4, 6, 3, 6, 2, 3, 1, 5, 7, 5, 7, 6, 5, 6]
print(list(set(rep_list)))


# Frozen Sets

x = frozenset([1, 2, 4, 6])
print(x, type(x))