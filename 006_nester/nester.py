
# movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
# ["Graham Chapman", ["Michael Palin", "John Cleese",
# "Terry Gillian", "Eric Idle", "Terry Jones"]]]

# def print_lol(the_list):
#   for each_item in the_list:
#     if isinstance(each_item, list):
#       print_lol(each_item)
#     else:
#       print(each_item)

# print_lol(movies)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gillian", "Eric Idle", "Terry Jones"]]]


def print_lol(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print("\t", end="")
            print(each_item)


print_lol(movies, 0)
