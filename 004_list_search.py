names = ["Michael", "Sarah", "John", "Anna", "David"]

# isinstance --> python BIF(Built-in Functions) 内置函数
flag = isinstance(names, list)
print(flag)

num_names = len(names)
flag1 = isinstance(num_names, tuple)
print(flag1)



movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
["Graham Chapman", ["Michael Palin", "John Cleese",
"Terry Gillian", "Eric Idle", "Terry Jones"]]]


for each_item in movies:
    if isinstance(each_item, list):
        for each_sub_item in each_item:
            print(f"Sub-item: {each_sub_item}")
    else:
        print(f"Item: {each_item}")
