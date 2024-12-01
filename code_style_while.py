my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = len(my_list)
y = 0
while x > y:
    if my_list[y] > 0:
        print(my_list[y])
        y += 1
    elif my_list[y] == 0:
        y += 1
        continue
    else:
        break
