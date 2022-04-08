colours = ["blue", "red", "green", "purple", "yellow"]

h = "hello"
print(h.upper())  # Method that RETURNS something
print(h)

print(colours.append("brown")) # Method that DOES NOT return something
print(colours)

print("---POP---")
print(colours.pop(0))
print(colours)

mixed = ["hello", 2342, 3.14, True, [1, 2, 3]]

print(mixed[-1][-1])
print(mixed)
mixed[0] = "goodbye"
print(mixed)
