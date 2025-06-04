# data = open('sketch.txt')
data = open(
    '/Users/fangxiang/Downloads/0636920003434-master/code/chapter3/sketch.txt')


# print(data.readline(), end='')

# print(data.readline(), end='')


data.seek(0)  # Reset the file pointer to the beginning of the file

for each_line in data:
    print(each_line, end='')

data.close()
