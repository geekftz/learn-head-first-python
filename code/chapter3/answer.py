man = []
other = []
# This code is a simplified version of the above code, focusing on reading a file and handling exceptions.

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            if role == 'Man':
                man.append(line_spoken.strip())
            elif role == 'Other Man':
                other.append(line_spoken.strip())
            # print(role, end='')
            # print(' said: ', end='')
            # print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')

print('Man:', man)
print('\n')
print('Other Man:', other)
