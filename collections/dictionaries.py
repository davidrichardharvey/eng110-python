# # Dictionaries
#
# # Key-Value Pairs
#
# me = {
#     "name": "David",
#     "job": "Trainer",
#     "age": 31
# }
#
# print(me, type(me))
#
# # DICTIONARY NAME [ KEY ]
# # print(me["job"])
# # me["job"] = "Zoo Keeper"
# # print(me)
# # me["hobbies"] = ["Video Games", "Board Games", "Comics", "Improv"]
# # print(me)
# #
# # print(me.get("name"))
# # me.update({"name": "D. R. Harvey", "job": "Trainer"})
# # print(me)
#
# # print(me["height"])
# # print(me.get("height"))
#
#
# # Make a dictionary with information about your favourite film
film = {
    'title': 'Shrek',
    'year': 2001,
    'studio': 'Dreamworks',
    'ratings': {
        'iMDb': 0.79,
        'Rotten Tomatoes': 0.88,
        'Metacritic': 0.84
    }
}
#
# print(film)
# print(film["ratings"]["iMDb"])


# Dictionary Methods

print(film.keys())
print(film.values())
items = film.items()
