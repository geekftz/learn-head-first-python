class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name


johnny = NamedList('Johnny')
# print(type(johnny))

# print(dir(johnny))

johnny.append('1:23.45')
print(johnny)

print(johnny.name)
